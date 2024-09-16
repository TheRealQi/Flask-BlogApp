from app import create_app, db
from flask_injector import FlaskInjector, singleton, inject


app = create_app()

if __name__ == '__main__':
    if app.config["CREATE_DATABASE_IF_NOT_FOUND"]:
        with app.app_context():
            db.create_all()
    app.run()