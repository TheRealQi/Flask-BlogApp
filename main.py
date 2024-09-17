from flask_injector import FlaskInjector, singleton
from flask_wtf import CSRFProtect
from werkzeug.security import generate_password_hash

from app import create_app, db
from app.models.user import User
from app.services.post import PostService
from app.services.user import UserService

app = create_app()
csrf = CSRFProtect(app)


def configure(binder):
    binder.bind(UserService, to=UserService(db), scope=singleton)
    binder.bind(PostService, to=PostService(db), scope=singleton)


FlaskInjector(app=app, modules=[configure])

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
