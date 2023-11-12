#!/bin/bash

source .venv/bin/activate
pip install --upgrade pip
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple zolltools==0.0.6.dev71
pip install -r requirements.txt
