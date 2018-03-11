import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = '5c7adad61fe0d6341c519df75102ae29'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')