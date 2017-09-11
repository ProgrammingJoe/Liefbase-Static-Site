from static_site import app, babel, mail
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

@app.route('/contact')
@app.route('/contact/<demo>', methods=['GET', 'POST'])
def contact(demo):
  form = ContactForm()
  form2 = DemoForm()

  demo = False if demo == '0' else True

  if request.method == 'POST':
    if form and form.validate() == False or form2 and form2.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form, form2=form2, demo=demo)
    elif form2 and form2.validate() == True:
      msg = Message("Demo Request", sender='liefbaseinfo@gmail.com', recipients=['liefbaseinfo@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return render_template('contact.html', success=True, demo=True)
    elif form and form.validate() == True:
      msg = Message(form.subject.data, sender='liefbaseinfo@gmail.com', recipients=['liefbaseinfo@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return render_template('contact.html', success=True, demo=False)
    else:
      return render_template('contact.html', form=form, form2=form2, demo=False)

  elif request.method == 'GET':
    return render_template('contact.html', form=form, form2=form2, demo=demo)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())
