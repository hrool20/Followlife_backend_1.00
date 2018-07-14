from .Default import Config


class LocalEnvironment(Config):
    DEBUG = True
    DATABASE_USER = 'root'
    DATABASE_PASSWORD = 'root'
    DATABASE_DB = 'fas'
    DATABASE_HOST = 'localhost'
