from flask import Flask, redirect
from dotenv import load_dotenv, dotenv_values
import os
from flask_jwt_extended import JWTManager

from src.controllers.home import home
from src.controllers.linenotify import linenotify
from src.controllers.auth import auth


# from werkzeug.middleware.proxy_fix import ProxyFix

#

load_dotenv()  # take environment variables from .env.


def create_app(config=None):

    # config = dotenv_values(".env")

    app = Flask(__name__, instance_relative_config=True)
    # app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_for=1)

    if config is None:
        line_notify_client_id = os.environ.get('LINE_NOTIFY_CLIENT_ID')
        line_notify_client_secret = os.environ.get('LINE_NOTIFY_CLIENT_SECRET')
        app_redirect_url = os.environ.get('APP_REDIRECT_URL')
        app_secret_key = os.environ.get('APP_SECRET_KEY')
        sqlalchemy_database_uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
        jwt_secret_key = os.environ.get('JWT_SECRET_KEY')
        # sqlalchemy_track_modifications = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
        # sqlalchemy_echo = os.environ.get('SQLALCHEMY_ECHO')

        app.config.from_mapping(
            LINE_NOTIFY_CLIENT_ID=line_notify_client_id,
            LINE_NOTIFY_CLIENT_SECRET=line_notify_client_secret,
            APP_REDIRECT_URL=app_redirect_url,
            APP_SECRET_KEY=app_secret_key,
            SQLALCHEMY_DATABASE_URI=sqlalchemy_database_uri,
            JWT_SECRET_KEY=jwt_secret_key
            # SQLALCHEMY_TRACK_MODIFICATIONS=sqlalchemy_track_modifications,
            # SQLALCHEMY_ECHO=sqlalchemy_echo == 'True'

            # SWAGGER={
            #     'title': "Bookmarks API",
            #     'uiversion': 3
            # }
        )

    else:
        app.config.from_mapping(config)

    JWTManager(app)

    app.register_blueprint(home)

    app.register_blueprint(linenotify)

    app.register_blueprint(auth)

    @app.route("/")
    def hello():
        return "line notify endpoints v1!"
    return app