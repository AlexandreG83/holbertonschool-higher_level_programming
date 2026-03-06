-- Creates the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creates the user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Grants only SELECT privilege on hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
