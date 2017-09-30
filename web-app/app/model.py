import pymysql
from flask import Flask, url_for, render_template, request, jsonify, redirect, flash


def connect():
    db = pymysql.connect(host='localhost', port=3306, user='root',
                         passwd='root', db='alexaforinstructions', cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    return db, cursor


def disconnect(db, cursor):
    cursor.close()
    db.close()


def check_user(email, password):
    db, cursor = connect()

    query = "SELECT email, password FROM users WHERE email = '%(email)s' AND password = '%(password)s'" % locals()
    cursor.execute(query)
    row = cursor.fetchone()

    disconnect(db, cursor)
    return row;

def email_exists(email):
    db, cursor = connect()

    query = "SELECT email FROM users WHERE email = '%(email)s'" % locals()
    cursor.execute(query)
    row = cursor.fetchone()

    disconnect(db, cursor)

    if (row == None):
        return False
    else:
        return True

def username_exists(email):
    db, cursor = connect()

    query = "SELECT email FROM users WHERE email = '%(email)s'" % locals()
    cursor.execute(query)
    row = cursor.fetchone()

    disconnect(db, cursor)

    if (row == None):
        return False
    else:
        return True

def add_user(firstname, lastname, email, username, password):
    error = None
    db, cursor = connect()
    try:
        query = "INSERT INTO users (firstname, lastname, email, password) VALUES ('%(firstname)s', '%(lastname)s', '%(email)s', '%(password)s')" % locals()
        cursor.execute(query)
        db.commit()
    except:
        error = "A database error has occurred. Please try again in a few minutes."
    disconnect(db, cursor)

    if (error):
        return(False, error)
    else:
        return(True, error);

def validate_pass(password):
    error = None
    if (password == ""):
        error = "Email address cannot be empty."
    elif (len(password) < 4):
        error = "Password must be at least 4 characters long."
    # elif (not password.isdigit()):
    #     error = "Password must include a digit (0-9)."
    # elif (not password.isupper()):
    #     error = "Password must include an uppercase letter (A-Z)."

    if (error):
        return(False, error)
    else:
        return(True, error);
