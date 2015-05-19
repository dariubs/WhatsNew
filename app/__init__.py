from flask import Flask, config

app = Flask(__name__, template_folder="templates", static_folder="static")

from app import views



