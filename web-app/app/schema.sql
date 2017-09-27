CREATE TABLE `alexaforinstructions`.`new_table` (
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`email`));

INSERT INTO users VALUES ("admin@example.com", "admin")

-- CREATE TABLE IF NOT EXISTS tasks (
--     task_id     int(11) NOT NULL AUTO_INCREMENT,
--     title       varchar(255) NOT NULL,
--     owner_id    int(11),
--     visibility  tinyint(1) NOT NULL,
--     UNIQUE (title),
--     PRIMARY KEY (set_id),
--     FOREIGN KEY (owner_id) REFERENCES users(user_id)
-- )ENGINE=InnoDB;
