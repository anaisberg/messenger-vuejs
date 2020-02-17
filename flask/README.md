# Flask

Python Flask allows to answer to HTTP queries easily.

## Installation

```shell
apt install python3-flask python3-anosql python3-venv mypy w3m sqlite3
```

## Tutorial and documentations

 - [Mega](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-now-with-python-3-support)
 - [AnoSQL](https://pypi.org/project/anosql/)
 - [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)

## Testing

Start server, log in `demons.log` is tailed on console:

```shell
make run
```

Test client:

```shell
browser http://127.0.0.1:5000/
```

Stop server when done:

```shell
make stop
```

## Note

There are two sets of SQL files, one for Sqlite3 and one for Postgres.

For DDL, some times, default values and so are not the same. Ok.

For DML queries through `anosql`, the sqlite version does not work with pg,
and vice versa, because 
[Python DB-API (PEP 249)](http://www.python.org/dev/peps/pep-0249/)
interface does *not* require to driver to implement a common parameter
passing scheme. Too bad.
