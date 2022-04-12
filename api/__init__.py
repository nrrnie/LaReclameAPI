from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    db.init_app(app)

    from api.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app
