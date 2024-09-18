from flask_sqlalchemy import SQLAlchemy
from app.models.post import Post
from app.models.postlike import PostLike
from app.models.postdislike import PostDislike
from flask_injector import inject
from flask_login import current_user


class PostService:
    @inject
    def __init__(self, sql: SQLAlchemy):
        self.sql = sql

    def get_by_id(self, post_id):
        return Post.query.get(post_id)

    def get_all_by_author_id(self, author_id):
        if current_user.id == author_id:
            return Post.query.filter_by(author_id=author_id).all()

    def get_all(self):
        return Post.query.all()

    def create(self, title, content, author_id):
        post = Post(
            author_id=author_id,
            title=title,
            content=content,
        )
        self.sql.session.add(post)
        self.sql.session.commit()
        return post

    def update(self, post_id, title, content):
        post = Post.query.get(post_id)
        post.title = title
        post.content = content
        self.sql.session.commit()
        return post

    def delete(self, post_id):
        if current_user.role == 'Admin' or (
                str(current_user.id) == str(Post.query.get(post_id).author_id) and current_user.role == 'Author'):
            post = Post.query.get(post_id)
            self.sql.session.delete(post)
            self.sql.session.commit()
        else:
            return 'You are not allowed to delete this post'

    def like(self, post_id):
        existing_like = PostLike.query.filter_by(post_id=post_id, user_id=current_user.id).first()
        existing_dislike = PostDislike.query.filter_by(post_id=post_id, user_id=current_user.id).first()
        if existing_like:
            self.sql.session.delete(existing_like)
            self.sql.session.commit()
        elif not existing_dislike:
            post_like = PostLike(post_id=post_id, user_id=current_user.id)
            self.sql.session.add(post_like)
            self.sql.session.commit()
        elif existing_dislike:
            self.sql.session.delete(existing_dislike)
            post_like = PostLike(post_id=post_id, user_id=current_user.id)
            self.sql.session.add(post_like)
            self.sql.session.commit()

    def dislike(self, post_id):
        existing_dislike = PostDislike.query.filter_by(post_id=post_id, user_id=current_user.id).first()
        existing_like = PostLike.query.filter_by(post_id=post_id, user_id=current_user.id).first()
        if existing_dislike:
            self.sql.session.delete(existing_dislike)
            self.sql.session.commit()
        elif not existing_like:
            post_dislike = PostDislike(post_id=post_id, user_id=current_user.id)
            self.sql.session.add(post_dislike)
            self.sql.session.commit()
        elif existing_like:
            self.sql.session.delete(existing_like)
            post_dislike = PostDislike(post_id=post_id, user_id=current_user.id)
            self.sql.session.add(post_dislike)
            self.sql.session.commit()

    def get_likes(self, post_id):
        return PostLike.query.filter_by(post_id=post_id).count()

    def get_dislikes(self, post_id):
        return PostDislike.query.filter_by(post_id=post_id).count()

    def is_liked_by_user(self, post_id):
        if PostLike.query.filter_by(post_id=post_id, user_id=current_user.id).first():
            return True
        else:
            return False

    def is_disliked_by_user(self, post_id):
        if PostDislike.query.filter_by(post_id=post_id, user_id=current_user.id).first():
            return True
        else:
            return False
