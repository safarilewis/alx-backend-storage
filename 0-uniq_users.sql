--creates users table with given attributes

CREATE TABLE IF NOT EXISTS users(
    id int NOT NULL AUTO_INCREMENT,
    UNIQUE email varchar(255) NOT NULL,
    name varchar(255),
);