from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init.app(app, db)

    #Blueprints
    from app.blueprints.public import public_bp
    from app.blueprints.public import auth_bp
    from app.blueprints.public import admin_bp

    app.register_blueprints.public(public_bp)
    app.register_blueprints.public(auth_bp, url_prefix='/auth')
    app.register_blueprints.public(auth_bp, url_prefix='/admin')

