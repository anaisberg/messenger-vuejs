#! /usr/bin/env python3

import typing
from DB import DB

#db = DB('sqlite3', 'test.db', 'test.sql')
db = DB('pg', 'dbname=demons', 'demons-pg.sql')
db.pull_demons('test', 1)
