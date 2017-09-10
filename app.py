from flask import Flask
from flask.ext.babel import Babel
from flask import render_template
from flask import g, request
from flask.ext.babel import gettext

app = Flask(__name__)

app.config.from_pyfile('config.py')
babel = Babel(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/pricing')
def pricing():
  return render_template('pricing.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())
