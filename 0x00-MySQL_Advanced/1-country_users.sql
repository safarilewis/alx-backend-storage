-- Creates a table users with given requirements.
DROP TABLE IF EXISTS users;
CREATE TABLE USERS(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    name VARCHAR(255),
    country ENUM('US','CO','TN') NOT NULL
);
