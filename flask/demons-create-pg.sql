-- for client portability, web build iso date strings
CREATE OR REPLACE FUNCTION isots(ts TIMESTAMP)
RETURNS TEXT IMMUTABLE STRICT AS $$
  SELECT UPPER(TO_CHAR(ts, 'YYYY-MM-DDtHH24:MI:SSz'));
$$ LANGUAGE SQL;

CREATE TABLE Demons(
  id SERIAL8 PRIMARY KEY,
  ts TIMESTAMP DEFAULT (NOW() AT TIME ZONE 'utc'),
  channel TEXT NOT NULL,
  content TEXT NOT NULL);

\i demons-data.sql
