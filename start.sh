#/bin/bash

export FLASK_APP=./static_site/__init__.py
export PYTHONPATH='./static_site/'
flask run --host=0.0.0.0 --port=33507
