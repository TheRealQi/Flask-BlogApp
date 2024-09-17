from flask_injector import FlaskInjector, singleton
from app import create_app, db, login_manager
from app.services.user import UserService

app = create_app()


def configure(binder):
    binder.bind(UserService, to=UserService(db), scope=singleton)


FlaskInjector(app=app, modules=[configure])


@login_manager.user_loader
def load_user(user_id):
    return UserService(db).get_by_id(user_id)


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    app.run(debug=True)
