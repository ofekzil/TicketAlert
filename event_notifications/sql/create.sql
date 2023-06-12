CREATE TABLE EventInfo(
    eventId INTEGER AUTO_INCREMENT,
    performerAndCity VARCHAR(300),
    eventDate DATE,
    eventUrl VARCHAR(400),
    threshold INTEGER,
    email VARCHAR(200),
    PRIMARY KEY(eventId),
    UNIQUE(eventUrl, threshold, email)
);


-- CREATE TABLE EventInfoNoId(
--     performerAndCity VARCHAR(300),
--     eventDate DATE,
--     eventUrl VARCHAR(400),
--     threshold INTEGER,
--     email VARCHAR(200),
--     PRIMARY KEY(eventUrl, threshold, email)
-- );

-- CREATE TABLE EventInfoOld(
--     performer VARCHAR(200),
--     venue VARCHAR(200),
--     eventDate DATE,
--     eventUrl VARCHAR(400),
--     threshold INTEGER,
--     email VARCHAR(200),
--     PRIMARY KEY(eventUrl, threshold, email)
-- );

-- example queries:
-- INSERT INTO EventInfo VALUES(...)
-- SELECT * FROM EventInfo WHERE DATE(eventDate) <= (SELECT CURDATE());
-- DELETE FROM EventInfo WHERE eventDate > (SELECT CURDATE());

