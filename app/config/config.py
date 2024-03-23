import os

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY') or \
        '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
    FLASK_SECRET = SECRET_KEY
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')


class ProdConfig(Config):
    FLASK_ENV = environ.get('FLASK_ENV')
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('DEFAULT_SQLALCHEMY_DATABASE_URI')


class DevConfig(Config):
    FLASK_ENV = environ.get('FLASK_ENV')
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('DEFAULT_SQLALCHEMY_DATABASE_URI') \
        or 'sqlite:///' + os.path.join(basedir, 'db.sqlite')


class TestConfig(Config):
    FLASK_ENV = environ.get('FLASK_ENV')
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test_db.sqlite')


CONFIGS = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig,
    "default": DevConfig
}
