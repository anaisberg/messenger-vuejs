# root makefile for demons project

.ONESHELL:
SHELL	= /bin/bash

# all subdirectories with makefiles
SUBS	= flask

# clean
clean: $(SUBS:%=%.clean)
	$(RM) -r venv

.PHONY: %.clean
%.clean:
	-dir=$(basename $@) && [ -f $$dir/Makefile ] && $(MAKE) -C $$dir clean

# curses? psycopg2
# setup python virtual environment
venv:
	python3 -m venv venv
	source venv/bin/activate
	pip install anosql flask ipython requests
