from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_required, current_user
from injector import inject

from app import db
from app.decorators import role_required
from app.forms.posts.create_edit_form import CreateEditPostForm
from app.forms.posts.delete_form import DeletePostForm
from app.services.post import PostService
from app.services.user import UserService

posts = Blueprint("posts", __name__)


@posts.route('/', methods=['GET'])
@inject
def list_all(post_service: PostService, user_service: UserService):
    delete_post_form = DeletePostForm()
    all_posts = post_service.get_all()
    for post in all_posts:
        post.author = user_service.get_by_id(post.author_id)
        post.author_username = post.author.username
        post.author_id = int(post.author_id)
    return render_template('posts/posts_list.html', posts=all_posts, form=delete_post_form)


@posts.route('/myposts', methods=['GET'])
@login_required
@inject
def list_author_posts(post_service: PostService, user_service: UserService):
    delete_post_form = DeletePostForm()
    author_id = current_user.id
    author_posts = post_service.get_all_by_author_id(author_id)
    for post in author_posts:
        post.author = user_service.get_by_id(post.author_id)
        post.author_username = post.author.username
        post.author_id = int(post.author_id)
    return render_template('posts/my_posts.html', posts=author_posts, form=delete_post_form)


@posts.route('/<int:post_id>', methods=['GET'])
@login_required
@inject
def view(post_service: PostService, post_id):
    delete_post_form = DeletePostForm()
    post = post_service.get_by_id(post_id)
    user_service = UserService(db)
    author_username = user_service.get_by_id(post.author_id).username
    post.author_username = author_username
    return render_template('posts/view_post.html', post=post, form=delete_post_form)


@posts.route('/create', methods=['POST', 'GET'])
@login_required
@inject
@role_required(['Admin', 'Author'])
def create(post_service: PostService):
    create_post_form = CreateEditPostForm()
    if create_post_form.validate_on_submit():
        post_service.create(create_post_form.title.data, create_post_form.content.data, current_user.id)
        return redirect(url_for('posts.list_author_posts'))
    return render_template('posts/create_post.html', form=create_post_form)


@posts.route('/<post_id>/edit', methods=['GET', 'POST'])
@login_required
@inject
@role_required(['Admin', 'Author'])
def edit(post_service: PostService, post_id):
    post = post_service.get_by_id(post_id)
    edit_post_form = CreateEditPostForm(obj=post)
    if edit_post_form.validate_on_submit():
        post_service.update(post_id, edit_post_form.title.data, edit_post_form.content.data)
        return redirect(url_for('posts.view', post_id=post_id))
    return render_template('posts/edit_post.html', form=edit_post_form, post_id=post_id)


@posts.route('/<int:post_id>/delete', methods=['POST'])
@login_required
@inject
@role_required(['Admin', 'Author'])
def delete(post_service: PostService, post_id):
    post_service.delete(post_id)
    return redirect(request.url)


@posts.route('/<int:post_id>/like', methods=['POST'])
@login_required
@inject
def like(post_service: PostService, post_id):
    return "Like a post"


@posts.route('/<int:post_id>/dislike', methods=['POST'])
@login_required
@inject
def dislike(post_service: PostService, post_id):
    return "Dislike a post"
