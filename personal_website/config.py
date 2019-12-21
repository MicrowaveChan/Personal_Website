# import os
import json
# with open for config_file
with open('/etc/flask-config.json') as config_file:
    config = json.load(config_file)

# os.environ.get for environment variables
class Config():
    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
