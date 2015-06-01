from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired

class LoginForm(Form):
	username = StringField("username")
	password = StringField("password")
	submit = SubmitField("Login")

class RegisterForm(Form):
	username = StringField("username")
	email = StringField("email")
	password = StringField("password")
	submit = SubmitField("Register")

class LinkForm(Form):
	title = StringField("title")
	url = StringField("url")
	submit = SubmitField("submit url")