from sqlalchemy.orm import backref

from app import sql


class PostLike(sql.Model):
    __tablename__ = 'post_like'
    user_id = sql.Column(sql.Integer, sql.ForeignKey('user.id'), primary_key=True)
    post_id = sql.Column(sql.Integer, sql.ForeignKey('post.id'), primary_key=True)
    # user = sql.relationship('User', backref=backref('likes'), lazy=True)
    # post = sql.relationship('Post', backref=backref('likes'), lazy=True)