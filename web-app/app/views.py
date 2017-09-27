from app import app
from app import model
from flask import Flask, url_for, render_template, request, jsonify, redirect, flash

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        result = model.check_user(request.form["email"], request.form["pasword"])
        if result == None:
            error='Invalid Credentials. Please try again.'
        else:
            return redirect(url_for("upload"))
    else:
        return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/register/validate', methods=['POST'])
def register():
    if request.method == 'POST':
        result = model.add_user(request.form["email"], request.form["password"], request.form["confirm"])
        flash(result[1])
    return render_template('register.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')
