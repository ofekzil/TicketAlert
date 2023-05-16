CREATE TABLE EventInfo(
    performer VARCHAR(200),
    venue VARCHAR(200),
    eventDate DATE,
    eventUrl VARCHAR(400),
    threshold INTEGER,
    email VARCHAR(200),
    PRIMARY KEY(eventUrl, threshold, email)
);

-- example queries:
-- INSERT INTO EventInfo VALUES(...)
-- SELECT * FROM EventInfo WHERE DATE(eventDate) <= (SELECT CURDATE());
-- DELETE FROM EventInfo WHERE eventDate > (SELECT CURDATE());
