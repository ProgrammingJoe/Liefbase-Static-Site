from flask import Flask
from flask_babel import Babel
from flask_mail import Mail
import sys

app = Flask(__name__)
babel = Babel(app)

app.config.from_pyfile('config.py')

app.secret_key = '\xc5\x10!1\x1c\xd1\xf7\x83yQ\x9b\x96\xdazx\x93\xf1\x94\x96c\x9c\x0b\x17\xb9'

mail = Mail()
mail.init_app(app)


import views
import forms
