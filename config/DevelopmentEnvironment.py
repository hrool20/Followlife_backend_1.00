from .Default import Config


class DevelopmentEnvironment(Config):
    DEBUG = False
    DATABASE_USER = 'bea3c415eaaaa7'
    DATABASE_PASSWORD = 'fd8cd26b'
    DATABASE_DB = 'heroku_351798eba9c5582'
    DATABASE_HOST = 'us-cdbr-iron-east-04.cleardb.net'
