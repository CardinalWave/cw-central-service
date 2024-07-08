create database cw_central_db

CREATE TABLE IF NOT EXISTS users (
    token VARCHAR(255)  PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(60) NOT NULL UNIQUE,
   	device VARCHAR(255) NOT NULL unique,
    session_id VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS groups (
    id VARCHAR(255) PRIMARY key UNIQUE,
    title VARCHAR(255) NOT NULL
);


CREATE TABLE IF NOT EXISTS users_groups (
    id VARCHAR(255) PRIMARY key UNIQUE,
    secure_email VARCHAR(255) NOT NULL,
    group_title VARCHAR(255) NOT NULL,
    group_id VARCHAR(255) NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

