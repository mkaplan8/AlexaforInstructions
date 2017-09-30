from app import app
from app import model
from flask import Flask, url_for, render_template, request, jsonify, redirect, flash
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
from validate_email import validate_email

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    success = False
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        result = model.check_user(email, password)
        if (result == None):
            error = 'Invalid Credentials. Please try again.'
        else:
            success = True;

    if (error):
        return render_template('login.html', error=error)
    else:
        if (success):
            return render_template('upload.html')
        else:
            return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    success = False
    if request.method == 'POST':
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        password = request.form["password"]
        confirm = request.form["confirm"]

        validEmail = validate_email(email)
        existingEmail = model.user_exists(email)
        validPass, passError = model.validate_pass(password)
        if (not validEmail):
            error = "Please use a valid email address."
        elif (not validPass):
            error = passError
        elif (existingEmail):
            error = "An account with email \"" + email + "\" already exists"
        elif (password != confirm):
            error = "Password and confirm password must match."
        else:
            success, error = model.add_user(email, password)

    if (error):
        return render_template('register.html', error=error)
    else:
        if (success):
            return render_template('upload.html')
        else:
            return render_template('register.html', error=error)

@app.route('/register/validate', methods=['GET', 'POST'])
def regValidate():
    return render_template('register.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')
