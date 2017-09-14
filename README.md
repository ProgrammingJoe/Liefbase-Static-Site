# Static Site

## Setup

* Clone project
  * `$ git clone git@gitlab.com:Liefbase/static_site.git`
* Create and activate a virtual environment
  * `$ pip3 install virtualenv`
  * `$ python3 -m virtualenv venv` or whatever name you want instead of venv.
  * `$ source venv/bin/activate`
* Install python dependencies
  * `$ pip3 install -r requirements.txt`
* Export and run project
  * `$ cd static_site`
  * `$ export FLASK_APP=__init__.py`
  * `$ flask run`
