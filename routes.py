# -*- coding: utf-8 -*-

"""
	WhatsNew
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
	return ":)"

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/submit/new")
def submit_new():
	return render_template("post.html")


if __name__ == '__main__':
	app.run()
