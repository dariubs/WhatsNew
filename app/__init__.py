from flask import Flask, render_template, redirect, url_for, abort, session, request, make_response
from forms import LoginForm, RegisterForm

from config import *

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.secret_key = "guess me"

from app import views