from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from api.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    from api.users import users
    app.register_blueprint(users, url_prefix='/users')

    with app.app_context():
        db.create_all()

    return app
