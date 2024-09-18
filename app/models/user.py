from flask_login import UserMixin
from app import sql


class User(sql.Model, UserMixin):
    __tablename__ = 'user'
    id = sql.Column(sql.Integer, primary_key=True)
    username = sql.Column(sql.String(120), unique=True, nullable=False)
    email = sql.Column(sql.String(120), unique=True, nullable=False)
    password = sql.Column(sql.String(120), nullable=False)
    role = sql.Column(sql.String(6), nullable=False, default='Reader')
    date_created = sql.Column(sql.DateTime, default=sql.func.current_timestamp())
    date_modified = sql.Column(
        sql.DateTime, default=sql.func.current_timestamp(),
        onupdate=sql.func.current_timestamp()
    )