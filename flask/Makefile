# all powerful makefile to start the demons service

.ONESHELL:
SHELL = /bin/bash

CHAN	= test
PS.pid	= processes.pid
DB		= demons
F.db	= $(DB).db
F.log	= $(DB).log

.PHONY: clean
clean: stop-ps
	$(RM) -r __pycache__ .mypy_cache
	$(RM) $(F.db) $(F.db)-journal $(F.log)
	dropdb $(DB) || exit 0

# databases initialization
$(F.db):
	sqlite3 $@ < demons-create-lite.sql

.PHONY: $(DB).pg
$(DB).pg:
	createdb $(DB)
	psql $(DB) < demons-create-pg.sql

# process management
.PHONY: run run-lite run-pg run-ps stop-ps stop

# start 3 processes, driven by environment variables:
# - Cleaner cleans entries periodically
# - Filler generates dummy entries periodically, for testing purposes
# - flask is the actual HTTP service
# file $(PS.pid) contains the process numbers to kill them on stop
run-ps:
	echo "# starting demons"
	./Cleaner.py >> $(F.log) 2>&1 &
	echo $$! >> $(PS.pid)
	./Filler.py $(CHAN) >> $(F.log) 2>&1 &
	echo $$! >> $(PS.pid)
	export APP_ROOT=$${APP_ROOT:-.}
	export FLASK_APP=demons.py FLASK_ENV=development
	flask run --host="0.0.0.0" >> $(F.log) 2>&1 &
	echo $$! >> $(PS.pid)

# start with sqlite backend, tail logs
run-lite: $(F.db)
	export DB_TYPE=sqlite3 DB_CONN=$(F.db) DB_SQL=demons-lite.sql
	$(MAKE) run-ps
	tail -f $(F.log)

# start service with postgres backend, tail logs
run-pg: $(DB).pg
	export DB_TYPE=pg DB_CONN="dbname=$(DB)" DB_SQL=demons-pg.sql
	$(MAKE) run-ps
	tail -f $(F.log)

# default is to run the sqlite version
run: run-lite

# stop service processes if running
stop-ps:
	echo "# stopping demons"
	[ -f $(PS.pid) ] && kill $$(cat $(PS.pid))
	$(RM) $(PS.pid)

stop: stop-ps

# development utils
.PHONY: type-check
type-check:
	mypy demons.py DB.py Cleaner.py Filler.py
