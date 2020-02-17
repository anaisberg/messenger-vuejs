#! /usr/bin/env python3

from typing import Dict
import logging
from os import environ as ENV

from DB import DB

logging.basicConfig(level=logging.INFO)
db = DB(ENV['DB_TYPE'], ENV['DB_CONN'], ENV['DB_SQL'])

# web app: depends on the environment
from flask import Flask, Response, jsonify, redirect
app = Flask('demons')

MIME: Dict[str,str] = {
	'html': 'text/html',
	'ico': 'image/x-ico',
	'js': 'text/javascript',
	'css': 'text/css'
}

# actual API
@app.route('/<channel>/pull')
def pull(channel: str):
	return jsonify([{ "id":r[0], "ts":r[1], "content":r[2] } for r in db.pull_demons(channel, 1)])

# pull recent stuff as a json list
@app.route('/<channel>/pull/<int:minid>')
def pull_id(channel: str, minid: int):
	return jsonify([{ "id":r[0], "ts":r[1], "content":r[2] } for r in db.pull_demons(channel, minid)])

# show some stuff
@app.route('/<channel>/get/<int:id>/')
def get(channel: str, id: int):
	try: # one row
		r = db.get_demons(channel, id)[0]
		return jsonify({ "id":r[0], "ts":r[1], "content":r[2] })
	except: # empty
		return jsonify(None)

# add an entry
@app.route('/<channel>/post/<path:content>')
def post(channel: str, content: str):
	db.post_demons(channel, content)
	db.commit()
	# this answer could be jsonified, for uniformity: causes light troubles in Android
	return "ok"

# web client for testing
@app.route('/')
def app_root():
	return redirect('demons.html')

# the suffix may still contain dots in it (this is the case in react-generated js files)
@app.route('/<path:path>.<suffix>')
def app_client(path: str = '', suffix: str = 'html'):
	if '..' in path:
		raise Exception("unexpected relative path: %s" % path)
	fullpath = "%s/%s.%s" % (ENV['APP_ROOT'], path, suffix)
	return Response(open(fullpath).read(), mimetype=MIME[suffix.split('.')[-1]])
