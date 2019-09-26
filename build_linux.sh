#!/bin/sh
pip install -r requirements.txt
pytest
python setup.py sdist