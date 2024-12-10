CREATE DATABASE main;
\c main;
CREATE TABLE messages (
    uuid VARCHAR(255) NOT NULL DEFAULT 'test',
    timestamp TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    messagecontent VARCHAR(5000) NOT NULL DEFAULT 'test',
    fromuser BOOLEAN NOT NULL DEFAULT FALSE,
    CHECK(EXTRACT(TIMEZONE FROM timestamp) = '0')
);

INSERT INTO messages (uuid, messagecontent) VALUES
    ('test', 'postgres testing messages'),
    ('test', 'if you are seeing this, the postgres initialization worked'),
    ('test', 'hooray!');

CREATE TABLE users (
	uuid VARCHAR(255) NOT NULL DEFAULT 'test',
	username VARCHAR(50) NOT NULL DEFAULT 'naoto',
	password VARCHAR(255) NOT NULL
	);
