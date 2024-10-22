-- Read user
-- Script that creates the database hbtn_0d_2 and the user user_0d_2

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON hbtn_0d_2. * TO 'user_0d_2'@'localhost';

-- Reload the grant tables to ensure that the new privileges are put into effect
FLUSH PRIVILEGES;
