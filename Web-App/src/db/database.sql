CREATE TABLE IF NOT EXISTS users (
    user_id     int(11) NOT NULL AUTO_INCREMENT,
    username    varchar(255) NOT NULL,
    email       varchar(255) NOT NULL,
    password    varchar(255) NOT NULL,
    logged_in   tinyint(1) NOT NULL,
    first_name  varchar(255) NOT NULL,
    last_name   varchar(255) NOT NULL,
    -- alexa_id    varchar(255),
    age         int(3) NOT NULL,
    UNIQUE (username),
    UNIQUE (email),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS instruction_sets (
    set_id      int(11) NOT NULL AUTO_INCREMENT,
    title       varchar(255) NOT NULL,
    owner_id    int(11),
    UNIQUE (title),
    PRIMARY KEY (set_id),
    FOREIGN KEY (owner_id) REFERENCES users(user_id)
);
