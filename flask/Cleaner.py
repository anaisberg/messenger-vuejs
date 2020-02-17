#! /usr/bin/env python3

import typing

from os import environ as ENV

import logging

from DB import DB

import time
import datetime as dt

import threading
from threading import Thread

"""
Cleaner Background Task
===

Periodically remove old entries from Demons.
"""
class Cleaner(Thread):

	def __init__(self, delay: float, db: DB, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._count = 0
		self._delay = delay
		self._db = db

	def run(self):
		logging.info("Cleaner is running...")
		# every delay/3, clean up to delay
		while True:
			time.sleep(self._delay / 3)
			self._count += 1
			t = dt.datetime.utcnow() - dt.timedelta(seconds=self._delay)
			upto = t.strftime("%Y-%m-%dT%H:%M:%SZ")
			try:
				logging.info("cleaning %d: %s" % (self._count, upto))
				self._db.clean_demons(upto)
				self._db.commit()
			except:
				logging.warning("clean %d failed" % self._count)
				pass

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	db = DB(ENV['DB_TYPE'], ENV['DB_CONN'], ENV['DB_SQL'])
	Cleaner(20.0, db).run()
