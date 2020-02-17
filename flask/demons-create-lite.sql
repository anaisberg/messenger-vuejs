CREATE TABLE Demons(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  -- sqlite does not have a timestamp type, we just build an iso date string
  ts TIMESTAMP DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ',CURRENT_TIMESTAMP)),
  channel TEXT NOT NULL,
  content TEXT);

.read demons-data.sql
