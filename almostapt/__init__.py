__version__ = '0.1.0'

from flask import Flask
from almostapt.main.routes import main
from almostapt.errorpages.errorhandlerpage import errorpages


def create_app(config_file="config.py"):

    app = Flask(__name__, static_folder="static")

    app.config.from_pyfile(config_file)

    app.register_blueprint(main)
    app.register_blueprint(errorpages)

    return app
