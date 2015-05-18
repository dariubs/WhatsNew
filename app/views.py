from app import app
from flask import Flask, render_template, redirect, url_for, abort, session, request, make_response, flash
from app.forms import LoginForm, RegisterForm

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

# Register
@app.route("/register", methods=['GET', 'POST'])
@app.route("/signup", methods=['GET', 'POST'])
def register():
	form = RegisterForm()

	if request.method == 'POST':
		return "Hi"

	return render_template("register.html", form=form)


# Login
@app.route("/login", methods=['GET', 'POST'])
@app.route("/signin", methods=['GET', 'POST'])
def login():
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
@app.route("/signout")
def logout() :
	if 'username' in session :
		session.pop('username', None)
		return redirect(url_for('home'))
	else :
		return redirect(url_for('login'))


# Submit Posts
@app.route("/submit/new")
def submit_new():
	if 'username' in session :
		return render_template("post.html")
	else  :
		flash('Login requested')
		return redirect(url_for('login'))


# User Page
@app.route("/@<username>")
def userpage(username = "null"):
	email = request.args.get("email"," ")
	return "Hello, {} , < {} >".format(username,email)


# 404
@app.errorhandler(404)
def not_found() :
	render_template("404.html"), 404

