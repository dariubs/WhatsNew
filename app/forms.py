from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class LoginForm(Form):
	username = StringField("username")
	password = StringField("password")

class RegisterForm(Form):
	username = StringField("username")
	password = StringField("password")  