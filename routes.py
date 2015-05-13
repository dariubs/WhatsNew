# -*- coding: utf-8 -*-

"""
	WhatsNew
"""

from flask import Flask, render_template, redirect, url_for, abort, session
from forms import LoginForm, RegisterForm
from flask import request


app = Flask(__name__)

app.secret_key = "guess me"

# Home
@app.route("/")
def home():
	if 'username' in session :
		return "Hello"
	else :
		return redirect(url_for('login'))

# Register
@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegisterForm()

	if request.method == 'POST':
		return "Hi"

	return render_template("register.html", form=form)


# Login
@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if request.method == 'POST':
		# Dummy Login
		if request.form["username"] == "admin" and request.form["password"] == "admin" :
			session["username"] = request.form["username"]
			return redirect(url_for('home'))
	return render_template("login.html", form=form)

# Logout
@app.route("/logout")
def logout() :
	if 'username' in session :
		session.pop('username', None)
		return redirect(url_for('home'))
	else :
		return redirect(url_for('login'))

# Submit Posts
@app.route("/submit/new")
def submit_new():
	return render_template("post.html")


# User Page
@app.route("/user/<username>")
def userpage(username):
	return "Hello, %s" % username

# 404
@app.errorhandler(404)
def not_found() :
	render_template("404.html"), 404


if __name__ == '__main__':
	app.debug = False
	app.run()
