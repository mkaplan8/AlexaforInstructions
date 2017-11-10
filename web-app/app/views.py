from app import app
from app import model
from flask import Flask, url_for, render_template, request, jsonify, redirect, flash
from passlib.hash import sha256_crypt

session = {
    "userID": "",
    "username": "",
    "firstname": ""
}

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = success = user = isEmail = None
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]
        isEmail = True if ("@" in user) else False
        success, error = model.valid_user(user, isEmail, password)

    if (success):
        userInfo = model.get_user("email", user) if isEmail else model.get_user("username", user)
        session["userID"] = userInfo["id"]
        session["username"] = userInfo["username"]
        session["firstname"] = userInfo["firstname"]
        return redirect(url_for("upload"))
    else:
        return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session["userID"] = ""
    session["username"] = ""
    session["firstname"] = ""
    return redirect(url_for("home"))


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

    if (success):
        return render_template("register.html", success="Successful!")
    else:
        return render_template("register.html", error=error)


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if (session["username"] != ""):
        error = success = None
        if request.method == "POST":
            title = request.form["title"]
            materials = request.form["materials"]
            visibility = 1 if (request.form.get("visibility") == "on") else 0
            steps = ""
            try:
                for i in range(1, 100):
                    if (request.form["step"+str(i)] == ""):
                        error = "Steps cannot be empty."
                        break
                    steps += "<~>" + request.form["step"+str(i)]
            except:
                pass
            if (title == ""):
                error = "Title cannot be empty."
            elif (materials == ""):
                error = "Materials cannot be empty."
            else:
                success, error = model.add_task(session["userID"], title, materials, steps, visibility)

        if (success):
            return render_template("upload.html", success="Successful!")
        else:
            return render_template("upload.html", error=error)
    else:
        return redirect(url_for("home"))

@app.route("/library")
def library():
    if (session["username"] != ""):
        return render_template("library.html")
    else:
        return redirect(url_for("home"))

@app.route('/library/tasks')
def getTasks():
    return jsonify({"tasks": model.get_tasks(session["userID"])})
