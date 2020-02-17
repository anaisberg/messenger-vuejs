-- name: pull-demons
SELECT id, ts, content
FROM Demons
WHERE channel = :channel
  AND id >= :id;

-- name: get-demons
SELECT id, ts, content
FROM Demons
WHERE channel = :channel
  AND id = :id;

-- name: clean-demons!
DELETE FROM Demons
WHERE ts < :upto;

-- name: post-demons!
INSERT INTO Demons(channel, content)
VALUES (:channel, :content);

-- name: get-status
SELECT val
FROM Status
WHERE key = :key;

-- name: set-status!
UPDATE Status
SET val = :val
WHERE key = :key;

-- name: count-posts
SELECT COUNT(*)
FROM Demons;
