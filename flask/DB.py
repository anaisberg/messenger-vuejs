#! /usr/bin/env python3
#
# Hide all database stuff in a class
#

import typing
import logging

class DB:

	def __init__(self, db: str, conn: str, queries: str):
		logging.info("creating DB for %s" % db)
		self._conn_str = conn
        # database connection, import only if required
		if db in ('sqlite3', 'sqlite'):
			import sqlite3 as sqlite
			self._conn = sqlite.connect(conn, check_same_thread=False)
			self._db = 'sqlite3'
		elif db in ('pg', 'postgres', 'postgresql', 'psycopg2'):
			import psycopg2 as pg # type: ignore
			self._conn = pg.connect(conn)
			self._db = 'psycopg2'
		else:
			# note: anosql supports sqlite & postgres
			raise Exception("unexpected db %s" % db)
        # SQL queries
		import anosql as sql # type: ignore
		# with (partial) backward compatibility…
		if not hasattr(sql, 'from_path'):
			sql.from_path = lambda q, d: sql.load_queries(d, q)
		self._queries = sql.from_path(queries, self._db)
		# forward queries with inserted database connection
		from functools import partial
		for q in self._queries.available_queries:
			setattr(self, q, partial(getattr(self._queries, q), self._conn))

	def commit(self):
		self._conn.commit()

	def rollback(self):
		self._conn.rollback()

	def __str__(self):
		return "connection to %s database (%s)" % (self._db, self._conn_str)
