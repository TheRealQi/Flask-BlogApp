from flask_injector import FlaskInjector, singleton
from flask_wtf import CSRFProtect
from werkzeug.security import generate_password_hash

from app import create_app, sql
from app.models.user import User
from app.services.post import PostService
from app.services.user import UserService

app = create_app()
csrf = CSRFProtect(app)


def configure(binder):
    if app.config["DATABASE"] == "SQL":
        binder.bind(UserService, to=UserService(sql), scope=singleton)
        binder.bind(PostService, to=PostService(sql), scope=singleton)


FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    app.run(debug=True)
