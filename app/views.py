from app import app
from flask import Flask, render_template, redirect, url_for, abort, session, request, make_response, flash,g
from app.forms import LoginForm, RegisterForm
from flask.ext.wtf import Form

from app.models import *


@app.before_request
def before_request():
	"""Connect to the database"""
	g.db = db
	g.db.connect()

@app.after_request
def after_request(response):
	g.db.close()
	return response


def loggedin():
	if 'username' in session :
		return True
	else:
		return False

# Home
@app.route("/")
def home():
	
	links = [
		{
			"title" : "Google ",
			"link" : "https://google.com",
			"points" : 12,
			"user" : "user1",
			"created" : 24
		},
		{
			"title" : "Facebook",
			"link" : "https://fb.com",
			"points" : 10,
			"user" : "user2",
			"created" : 29
		},
		{
			"title" : "Twitter",
			"link" : "https://twitter.com",
			"points" : 9,
			"user" : "user3",
			"created" : 98
		}
	]

	return render_template("home.html", links = links)

# Pages
@app.route("/page/<int:num>")
def paginate(num):
	return "page {}".format(num)


"""
	User Registration
"""
@app.route("/register", methods=['GET', 'POST'])
def register():
	if loggedin():
		flash("You are logged in")
		return redirect("/")

	form = RegisterForm()
	if request.method == 'POST' :
		post_username = request.form["username"]
		post_email = request.form["email"]
		post_password = request.form["password"]

		if(User.not_username(post_username) and User.not_email(post_email)) :
			if(len(post_password) < 8):
				flash("password must be longer than 8 characters")
			else :
				User.create_user(post_username, post_email, post_password)
				return redirect(url_for('login'))
				

	return render_template("register.html", form=form)


# Login
@app.route("/login", methods=['GET', 'POST'])
def login():
	if loggedin():
		flash("You are logged in")
		return redirect("/")


	form = LoginForm()

	if request.method == 'POST':
		# Dummy Login
		if request.form["username"] == "admin" and request.form["password"] == "admin" :
			session["username"] = request.form["username"]
			return redirect(url_for('home'))
		else :
			flash("username & password are incorrect")
			render_template("login.html", form=form)
	return render_template("login.html", form=form)

# Logout
@app.route("/logout")
# @app.route("/signout")
def logout() :
	if loggedin() :
		session.pop('username', None)
		return redirect(url_for('home'))
	else :
		return redirect(url_for('login'))


# Submit Posts
@app.route("/submit/new")
def submit_new():
	if loggedin() :
		return render_template("post.html")
	else  :
		flash('Login requested')
		return redirect(url_for('login'))


# User Page
@app.route("/@<username>")
def userpage(username = "null"):
	email = request.args.get("email"," ")
	user = User.user_info(username)
	if user:
		return render_template("profile.html", user=user)
	else :
		return render_template("404.html")


# 404
@app.errorhandler(404)
def not_found() :
	render_template("404.html"), 404

