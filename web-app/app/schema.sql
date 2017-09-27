CREATE TABLE IF NOT EXISTS users (
    -- user_id     int(11) NOT NULL AUTO_INCREMENT,
    -- username    varchar(255) NOT NULL,
    email       varchar(255) NOT NULL,
    password    varchar(255) NOT NULL,
    -- logged_in   tinyint(1) NOT NULL,
    -- first_name  varchar(255) NOT NULL,
    -- last_name   varchar(255) NOT NULL,
    -- alexa_id    varchar(255),
    -- age         int(3) NOT NULL,
    -- UNIQUE (username),
    PRIMARY KEY (email),
    -- PRIMARY KEY (user_id)
)ENGINE=InnoDB;

-- CREATE TABLE IF NOT EXISTS tasks (
--     task_id     int(11) NOT NULL AUTO_INCREMENT,
--     title       varchar(255) NOT NULL,
--     owner_id    int(11),
--     visibility  tinyint(1) NOT NULL,
--     UNIQUE (title),
--     PRIMARY KEY (set_id),
--     FOREIGN KEY (owner_id) REFERENCES users(user_id)
-- )ENGINE=InnoDB;
