from datetime import timedelta

from flask import Flask
from flask_jwt_extended.jwt_manager import JWTManager

from app.models.BaseClasses import BaseResponse


def create_app(my_env, app_config_file):
    app = Flask(__name__, instance_relative_config=True)
    configure_environment(app, my_env, app_config_file)

    # JWT
    app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
    app.config['JWT_SECRET_KEY'] = 'followlife'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)
    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def expired_token_callback():
        return BaseResponse.unauthorized_response('Expired token.')

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return BaseResponse.unauthorized_response('Invalid token: ' + error)

    @jwt.unauthorized_loader
    def unauthorized_callback(error):
        return BaseResponse.unauthorized_response(error)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
