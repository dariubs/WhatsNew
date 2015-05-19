from flask import Flask, config
from flask.ext.gravatar import Gravatar

app = Flask(__name__, template_folder="templates", static_folder="static")

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    use_ssl=False,
                    base_url=None)

from app import views





