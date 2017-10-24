from static_site import app, babel, mail
from forms import ContactForm, DemoForm
from flask import render_template, request, flash
from flask_mail import Message
from flask_babel import gettext

@app.route('/')
def index():
  language = request.accept_languages.best_match(app.config['LANGUAGES'].keys())
  if language == 'fr':
      french = True
  else:
      english = True
  return render_template('index.html', **locals())

@app.route('/donate')
def donate():
  language = request.accept_languages.best_match(app.config['LANGUAGES'].keys())
  if language == 'fr':
    french = True
  else:
    english = True
  return render_template('donate.html', **locals())

@app.route('/about')
def about():
  language = request.accept_languages.best_match(app.config['LANGUAGES'].keys())
  if language == 'fr':
    french = True
  else:
    english = True
  return render_template('about.html', **locals())

@app.route('/contact')
@app.route('/contact/<demo>', methods=['GET', 'POST'])
def contact(demo):
  language = request.accept_languages.best_match(app.config['LANGUAGES'].keys())
  if language == 'fr':
    french = True
  else:
    english = True
  form = ContactForm()
  form2 = DemoForm()

  demo = False if demo == '0' else True

  if request.method == 'POST':
    if form and form.validate() == False and demo == False or form2 and form2.validate() == False and demo == True:
      error_message = gettext('All fields are required and e-mail must be valid')
      flash(error_message)
      return render_template('contact.html', **locals())
    elif form2 and form2.validate() == True:
      msg = Message("Demo Request", sender='liefbaseinfo@gmail.com', recipients=['liefbaseinfo@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      success = True
      return render_template('contact.html', **locals())
    elif form and form.validate() == True:
      msg = Message(form.subject.data, sender='liefbaseinfo@gmail.com', recipients=['liefbaseinfo@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      success = True
      return render_template('contact.html', **locals())
    else:
      return render_template('contact.html', **locals())

  elif request.method == 'GET':
    return render_template('contact.html', **locals())

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())
