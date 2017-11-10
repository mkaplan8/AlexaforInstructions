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
