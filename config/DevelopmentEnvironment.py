from .Default import Config


class DevelopmentEnvironment(Config):
    DEBUG = False
    DATABASE_USER = ''
    DATABASE_PASSWORD = ''
    DATABASE_DB = ''
    DATABASE_HOST = ''
