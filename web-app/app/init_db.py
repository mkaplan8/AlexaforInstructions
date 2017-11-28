import json
import sqlite3
from sqlite3 import Error

def connect():
    try:
        db = sqlite3.connect("a4i.db")
        cursor = db.cursor()
        return db, cursor
    except Error as e:
                print(e)
    return None

def disconnect(db, cursor):
    cursor.close()
    db.close()

def execute(statement):
    try:
        db, cursor = connect()
        cursor.execute(statement)
        db.commit()
    except Error as e:
        print(e)
    disconnect(db, cursor)

def main():
    create_users_table = ''' CREATE TABLE IF NOT EXISTS users (
                                id integer PRIMARY KEY NOT NULL,
                                firstname text NOT NULL,
                                lastname text NOT NULL,
                                email text NOT NULL UNIQUE,
                                username text NOT NULL UNIQUE,
                                password text NOT NULL
                            ); '''

    create_tasks_table = ''' CREATE TABLE IF NOT EXISTS tasks (
                                id integer PRIMARY KEY NOT NULL,
                                author_id integer NOT NULL,
                                title text NOT NULL,
                                materials text NOT NULL,
                                steps text NOT NULL,
                                visibility TINYINT(1) NOT NULL,
                                FOREIGN KEY (author_id) REFERENCES users(id)
                                    ON DELETE CASCADE
                                    ON UPDATE CASCADE
                            ); '''

    create_owners_table = ''' CREATE TABLE IF NOT EXISTS owners (
                                user_id integer NOT NULL,
                                task_id integer NOT NULL,
                                PRIMARY KEY (user_id, task_id),
                                FOREIGN KEY (user_id) REFERENCES users(id)
                                    ON DELETE CASCADE
                                    ON UPDATE CASCADE,
                                FOREIGN KEY (task_id) REFERENCES tasks(id)
                                    ON DELETE CASCADE
                                    ON UPDATE CASCADE
                            ); '''

    insert_user_admin = ''' INSERT INTO users (
                                firstname, lastname, email, username, password
                            ) VALUES (
                                "admin", "admin", "admin@example.com", "admin", "admin"
                            ); '''

    insert_task_admin = ''' INSERT INTO tasks (
                                author_id, title, materials, steps, visibility
                            ) VALUES (
                                (SELECT id from users order by id desc limit 1), "How to Admin", "Administrative Access", '["Ban users that are annoying.", "Ban users that are not annoying.", "Demonstrate unrivaled power."]', 1
                            ); '''

    execute(create_tasks_table)
    execute(create_users_table)
    execute(create_owners_table)
    execute(insert_user_admin)
    execute(insert_task_admin)

    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
