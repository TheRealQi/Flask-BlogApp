from flask_injector import FlaskInjector, singleton
from flask_wtf import CSRFProtect
from app import create_app, db
from app.services.user import UserService

app = create_app()
csrf = CSRFProtect(app)


def configure(binder):
    binder.bind(UserService, to=UserService(db), scope=singleton)


FlaskInjector(app=app, modules=[configure])

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
