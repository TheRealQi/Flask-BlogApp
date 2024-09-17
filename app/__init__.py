from flask import Flask, url_for, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    Bootstrap(app)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @app.context_processor
    def template_global_variables():
        return {
            'url_for': url_for,
            'get_flashed_messages': get_flashed_messages
        }

    from app.routes.dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)

    from app.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app
