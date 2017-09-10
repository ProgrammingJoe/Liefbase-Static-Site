from flask import Flask
app = Flask(__name__)

from flask import render_template

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
