#/bin/bash

export FLASK_APP=./static_site/__init__.py
export PYTHONPATH='./static_site/'
flask run --port=33507
