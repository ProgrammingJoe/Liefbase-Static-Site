#/bin/bash

export FLASK_APP=__init__.py
cd ./static_site/ && export PYTHONPATH='.' && flask run --host=0.0.0.0 --port=33507
