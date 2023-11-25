#!/bin/bash

python3 -m venv venv && source venv/bin/activate
pip install -r ./downloader/requirements/requirements.txt
python3 ./downloader/src/main.py
 