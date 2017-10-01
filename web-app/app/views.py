from app import app
from app import model
from flask import Flask, url_for, render_template, request, jsonify, redirect, flash
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = success = isEmail = None
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]
        isEmail = True if ("@" in user) else False
        success, error = model.valid_user(user, isEmail, password)

    if (error):
        return render_template("login.html", error=error)
    else:
        if (success):
            userInfo = model.get_user("email", user) if isEmail else model.get_user("username", user)
            return render_template("upload.html", fname=userInfo['firstname'])
        else:
            return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    error = success = None
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        confirm = request.form["confirm"]

        emailValid, emailError = model.valid_email(email)
        unameValid, unameError = model.valid_uname(username)
        passValid, passError = model.valid_pass(password, confirm)
        if (not emailValid):
            error = emailError
        elif (firstname == ""):
            error = "First name cannot be empty."
        elif (lastname == ""):
            error = "Last name cannot be empty."
        elif (not unameValid):
            error = unameError
        elif (not passValid):
            error = passError
        else:
            success, error = model.add_user(firstname, lastname, email, username, password)

    if (error):
        return render_template("register.html", error=error)
    else:
        if (success):
            return render_template("upload.html", fname=firstname)
        else:
            return render_template("register.html", error=error)


@app.route("/upload")
def upload():
    return render_template("upload.html", fname="testing")
