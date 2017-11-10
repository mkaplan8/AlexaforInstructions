DROP DATABASE alexaforinstructions;

CREATE DATABASE alexaforinstructions;

CREATE TABLE alexaforinstructions.users (
    id INT NOT NULL AUTO_INCREMENT,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    username VARCHAR(45) NOT NULL,
    password VARCHAR(45) NOT NULL,
    UNIQUE(email),
    UNIQUE(username),
    PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE alexaforinstructions.tasks (
    id INT NOT NULL AUTO_INCREMENT,
    author_id INT(11),
    title VARCHAR(255) NOT NULL,
    materials VARCHAR(1000),
    steps VARCHAR(10000),
    visibility TINYINT(1) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE alexaforinstructions.owners (
    user_id INT(11) NOT NULL,
    task_id INT(11) NOT NULL,
    PRIMARY KEY (user_id, task_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (task_id) REFERENCES tasks(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=InnoDB;

INSERT INTO alexaforinstructions.users (
    firstname, lastname, email, username, password
) VALUES (
    "admin", "admin", "admin@example.com", "admin", "admin"
);

INSERT INTO alexaforinstructions.tasks (
    author_id, title, materials, steps, visibility
) VALUES (
    (SELECT id from users order by id desc limit 1), "How to Admin", "Administrative Access", "<~>Ban users that are annoying.<~>Ban users that are not annoying.<~>Demonstrate unrivaled power.", 1
);
