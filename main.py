from app import create_app, db, login_manager
from flask_injector import FlaskInjector, singleton, inject

from app.services.user import UserService

app = create_app()


def configure(binder):
    binder.bind(UserService, to=UserService(db), scope=singleton)


@login_manager.user_loader
def load_user(user_id):
    return UserService(db).get_by_id(user_id)


if __name__ == '__main__':
    if app.config["CREATE_DATABASE_IF_NOT_FOUND"]:
        with app.app_context():
            db.create_all()
    app.run()
