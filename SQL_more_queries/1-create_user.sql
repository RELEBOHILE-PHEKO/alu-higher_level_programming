-- Creates the MySQL server user user_0d_1 with all privileges if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Display the grants for the user user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';
