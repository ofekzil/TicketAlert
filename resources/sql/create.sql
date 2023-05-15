CREATE TABLE EventInfo(
    performer VARCHAR(100),
    venue VARCHAR(150),
    eventDate DATE,
    eventUrl VARCHAR(200),
    threshold INTEGER,
    email VARCHAR(100),
    PRIMARY KEY(eventUrl, threshold, email)
);

-- example queries:
-- INSERT INTO EventInfo VALUES(...)
-- SELECT * FROM EventInfo WHERE DATE(eventDate) <= (SELECT CURDATE());
-- DELETE FROM EventInfo WHERE eventDate > (SELECT CURDATE());

