# Personal_Website
Personal Website build with HTML/ CSS/ Bootstrap and Flask.
Still a work in progress.

[Live version](http://www.robertmichaud.xyz) deployed using nginx and gunicorn.

## Getting Started
- git clone
- setup python3 virtualenv and install requirements
- setup config file or environment variables
- run development server
- navigate to http://localhost:5000
```
python3 run.py
```

## Requirements
*See requirements.txt and config.py*

###Python3 virtualenv
```
# virtualenv setup
virtualenv -p python3 venv
source venv/bin/activate

# now using virtualenv
pip install -r requirements.txt
```
###app config
With environment variables
```
# using environment variables
import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
```
With a config.json file
```
# using a config.json file
import json
with open('/etc/flask-config.json') as config_file:
    config = json.load(config_file)

class Config():
    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')	
```

