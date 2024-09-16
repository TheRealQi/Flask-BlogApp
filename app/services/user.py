from app.models.user import User
from flask_login import login_user, logout_user
from flask_injector import inject
from werkzeug.security import generate_password_hash, check_password_hash


class UserService:
    @inject
    def __init__(self, db):
        self.db = db

    def login(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return user
        return None

    def signup(self, username, email, password):
        hashed_password = generate_password_hash(password)
        user = User(
            username=username,
            email=email,
            password=password
        )
        self.db.session.add(user)
        self.db.session.commit()
        return user

    def logout(self):
        logout_user()
