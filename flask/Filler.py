#! /usr/bin/env python3
#
# a database filling thread for testing purposes
#

import typing
import logging
import random
import time
import threading
from threading import Thread
from os import environ as ENV

from DB import DB

class Filler(Thread):

	def __init__(self, delay: float, db: DB, chan: str, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._delay = delay
		self._db = db
		self._chan = chan
		self._count = 0
		self._rand = random.Random()

	def run(self):
		logging.info("Filler is running...")
		λ = 1.0 / self._delay
		while True:
            # fill
			self._count += 1
			logging.info("filler: %d" % self._count)
			try:
				self._db.post_demons(self._chan, "added message %d" % self._count)
				self._db.commit()
			except:
				logging.warning("filler %d failed" % self._count)
            # & wait
			delay = self._rand.expovariate(λ)
			if delay > 3 * self._delay: # truncate if too large
				delay = self._delay
			time.sleep(delay)

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	db = DB(ENV['DB_TYPE'], ENV['DB_CONN'], ENV['DB_SQL'])
	import sys
	chan = sys.argv[1] if len(sys.argv) >= 2 else 'filler'
	Filler(10.0, db, chan).run()
