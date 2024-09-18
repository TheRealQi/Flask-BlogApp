from sqlalchemy.orm import backref

from app import sql


class Post(sql.Model):
    __tablename__ = 'post'
    id = sql.Column(sql.Integer, primary_key=True)
    author_id = sql.Column(sql.Integer, sql.ForeignKey('user.id'), nullable=False)
    title = sql.Column(sql.String(120), nullable=False)
    content = sql.Column(sql.String(120), nullable=False)
    date_created = sql.Column(sql.DateTime, default=sql.func.current_timestamp())
    date_modified = sql.Column(
        sql.DateTime, default=sql.func.current_timestamp(),
        onupdate=sql.func.current_timestamp()
    )
    author = sql.relationship('User', backref=backref('posts'), lazy=True)
