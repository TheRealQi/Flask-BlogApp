from sqlalchemy.orm import backref

from app import sql


class PostDislike(sql.Model):
    __tablename__ = 'post_dislike'
    user_id = sql.Column(sql.Integer, sql.ForeignKey('user.id'), primary_key=True)
    post_id = sql.Column(sql.Integer, sql.ForeignKey('post.id'), primary_key=True)
    # user = sql.relationship('User', backref=backref('dislikes'), lazy=True)
    # post = sql.relationship('Post', backref=backref('dislikes'), lazy=True)
