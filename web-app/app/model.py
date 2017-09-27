import pymysql
from flask import Flask, url_for, render_template, request, jsonify, redirect, flash

def connect():
    db = pymysql.connect(host='localhost', port=3306, user='root',
                         passwd='', db='', cursorclass=pymysql.cursors.DictCursor)
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


def add_user(email, password, confirm):
    db, cursor = connect()

    if emailaddress == "":
        return(False, "Registration Failed: Empty Email")

    if password == "":
        return(False, "Registration Failed: You must enter a password.")

    if password != confirm:
        return(False, "Registration Failed: Password does not match confirmation")

    try:
        query = "INSERT INTO users (email, password) VALUES ('%(email)s', '%(password)s')" % locals()
        cursor.execute(query)
        db.commit()
    except:
        return(False, "Registration Failed: There was a problem with your registration.")

    disconnect(db, cursor)
    return (True, "Registration Successful!")
