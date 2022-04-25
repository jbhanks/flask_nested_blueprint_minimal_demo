"""Flask configuration."""
import os
from os import environ, path
from decouple import config
from dotenv import load_dotenv



basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    FLASK_APP = 'wsgi.py'
    FLASK_ENV = environ.get('FLASK_ENV')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    # Flask-Assets
    LESS_BIN = environ.get('LESS_BIN')
    ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')


class DeploymentConfig(Config):
    FLASK_ENV = 'Deployment'
    DEBUG = False
    TESTING = False
    SERVER_NAME='example.com'





