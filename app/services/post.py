from flask_sqlalchemy import SQLAlchemy
from app.models.post import Post
from flask_injector import inject
from flask_login import current_user


class PostService:
    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_by_id(self, post_id):
        return Post.query.get(post_id)

    def get_all_by_author_id(self, author_id):
        return Post.query.filter_by(author_id=author_id).all()

    def get_all(self):
        return Post.query.all()

    def create(self, title, content, author_id):
        post = Post(
            author_id=author_id,
            title=title,
            content=content,
        )
        self.db.session.add(post)
        self.db.session.commit()
        return post

    def update(self, post_id, title, content):
        post = Post.query.get(post_id)
        post.title = title
        post.content = content
        self.db.session.commit()
        return post

    def delete(self, post_id):
        if current_user.role == 'Admin' or (
                str(current_user.id) == str(Post.query.get(post_id).author_id) and current_user.role == 'Author'):
            post = Post.query.get(post_id)
            self.db.session.delete(post)
            self.db.session.commit()
        else:
            print("You are not allowed to delete this post.")

    def get_by_author(self, author_id):
        return Post.query.filter_by(id=author_id).all()
