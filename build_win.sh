#!/bin/sh
choco install -y python
export PATH=/c/Python37:$PATH
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
pytest
python setup.py sdist