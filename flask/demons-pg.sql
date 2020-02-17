-- name: pull-demons
SELECT id, isots(ts), content
FROM Demons
WHERE channel = %s
  AND id >= %s;

-- name: get-demons
SELECT id, isots(ts), content
FROM Demons
WHERE channel = %s
  AND id = %s;

-- name: clean-demons!
DELETE FROM Demons
WHERE ts <= %s;

-- name: post-demons!
INSERT INTO Demons(channel, content)
VALUES (%s, %s);

-- name: get-status
SELECT val
FROM Status
WHERE key = %s;

-- name: set-status!
UPDATE Status
SET val = %s
WHERE key = %s;

-- name: count-posts
SELECT COUNT(*)
FROM Demons;
