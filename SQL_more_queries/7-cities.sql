-- Creates the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Selects the database
USE hbtn_0d_usa;

-- Creates the table cities if it does not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
