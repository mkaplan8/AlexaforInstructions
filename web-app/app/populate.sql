INSERT INTO alexaforinstructions.users (
    firstname, lastname, email, username, password
) VALUES (
    "admin", "admin", "admin@example.com", "admin", "admin"
);
SELECT * FROM users;

INSERT INTO alexaforinstructions.tasks (
    author_id, title, materials, steps, visibility
) VALUES (
    (SELECT id from users order by id desc limit 1), "title", "materials", "steps", 1
);
