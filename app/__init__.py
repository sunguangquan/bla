from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_migrate import Migrate
from flask_admin import Admin

db = SQLAlchemy()
migrate = Migrate()
admin = Admin(name='bla')


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from app.routes import api
    app.register_blueprint(api)
    db.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db)
    return app
