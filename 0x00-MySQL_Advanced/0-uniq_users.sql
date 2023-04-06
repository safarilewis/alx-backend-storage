--creates users table with given attributes
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    UNIQUE email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
);