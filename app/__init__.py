from flask import Flask, url_for, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap

sql = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    sql.init_app(app)
    with app.app_context():
        sql.create_all()

    Bootstrap(app)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import User
        return User.query.get(user_id)

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

    from app.routes.users import users as users_blueprint
    app.register_blueprint(users_blueprint, url_prefix="/users")

    from app.routes.posts import posts as posts_blueprint
    app.register_blueprint(posts_blueprint, url_prefix="/posts")

    from app.routes.errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint, url_prefix="/errors")

    return app
