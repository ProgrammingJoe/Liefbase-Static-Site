from static_site import app, babel
from forms import ContactForm, DemoForm
from flask import render_template, request, flash
from flask_mail import Message

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/pricing')
def pricing():
  return render_template('pricing.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
  form2 = DemoForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)

  elif request.method == 'GET':
    return render_template('contact.html', form=form)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())
