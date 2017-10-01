import pymysql
from flask import Flask, url_for, render_template, request, jsonify, redirect, flash
from validate_email import validate_email


### --- CONNECT FUNCTIONS: --- ###

def connect():
    db = pymysql.connect(host="localhost", port=3306, user="root",
                         passwd="root", db="alexaforinstructions",
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    return db, cursor

def disconnect(db, cursor):
    cursor.close()
    db.close()


### --- ADD FUNCTIONS: --- ###

def add_user(firstname, lastname, email, username, password):
    error = None
    firstname = firstname.capitalize()
    lastname = lastname.capitalize()
    db, cursor = connect()
    try:
        query = "INSERT INTO users (firstname, lastname, email, username, password) VALUES ('%(firstname)s', '%(lastname)s', '%(email)s', '%(username)s', '%(password)s')" % locals()
        cursor.execute(query)
        db.commit()
    except:
        error = "A database error has occurred. Please try again in a few minutes."
    disconnect(db, cursor)

    if (error):
        return(False, error)
    else:
        return(True, error);

def add_task(title, materials, steps, visibility):
    error = None
    db, cursor = connect()
    try:
        query = "INSERT INTO tasks (title, materials, steps, visibility) VALUES ('%(title)s', '%(materials)s', '%(steps)s', '%(visibility)s')" % locals()
        cursor.execute(query)
        db.commit()
    except:
        error = "A database error has occurred. Please try again in a few minutes."
    disconnect(db, cursor)

    if (error):
        return(False, error)
    else:
        return(True, error);


### --- QUERY FUNCTIONS: --- ###

def get_user(queryType, query):
    db, cursor = connect()
    query = "SELECT * FROM users WHERE %(queryType)s = '%(query)s'" % locals()
    cursor.execute(query)
    row = cursor.fetchone()
    disconnect(db, cursor)
    return row


### --- BOOLEAN FUNCTIONS: --- ###

def email_exists(email):
    if (get_user("email", email) == None):
        return False
    else:
        return True

def username_exists(username):
    if (get_user("username", username) == None):
        return False
    else:
        return True

def user_exists(user, password):
    db, cursor = connect()
    query = "SELECT * FROM users WHERE (email = '%(user)s' OR username = '%(user)s') AND password = '%(password)s'" % locals()
    cursor.execute(query)
    row = cursor.fetchone()
    disconnect(db, cursor)

    if (row == None):
        return False
    else:
        return True


### --- VALIDATOR FUNCTIONS: --- ###

def valid_user(user, isEmail, password):
    error = None
    if (user == ""):
        error = "Email/username field cannot be empty."
    elif (password == ""):
        error = "Password field cannot be empty."
    elif ((not email_exists(user)) if isEmail else (not username_exists(user))):
        error = "A user by that email or username does not exist."
    elif (not user_exists(user, password)):
        error = "Incorrect password."

    if (error):
        return(False, error)
    else:
        return(True, error);

def valid_email(email):
    error = None
    if (email == ""):
        error = "Email field cannot be empty."
    elif (not validate_email(email)):
        error = "Please provide a valid email."
    elif (email_exists(email)):
        error = "This email already has an account associated with it."

    if (error):
        return(False, error)
    else:
        return(True, error);

def valid_uname(username):
    error = None
    if (username == ""):
        error = "Username field cannot be empty."
    elif (username_exists(username)):
        error = "This username has been taken."

    if (error):
        return(False, error)
    else:
        return(True, error);

def valid_pass(password, confirm):
    error = None
    if (password == ""):
        error = "Password cannot be empty."
    elif (len(password) < 4):
        error = "Password must be at least 4 characters long."
    # elif (not password.isdigit()):
    #     error = "Password must include a digit (0-9)."
    # elif (not password.isupper()):
    #     error = "Password must include an uppercase letter (A-Z)."
    elif (password != confirm):
        error = "Password and confirm password must match."

    if (error):
        return(False, error)
    else:
        return(True, error);

### --- HELPER FUNCTIONS: --- ###
