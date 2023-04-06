-- Creates a table users with given requirements.
DROP TABLE IF EXISTS users;
CREATE TABLE USERS(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE,
    name VARCHAR(255),
    country ENUM('US','CO','TN') DEFAULT 'US' NOT NULL
);
