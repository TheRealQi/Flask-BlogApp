from flask import Blueprint, render_template, request, redirect, url_for
from flask_injector import inject
from flask_login import login_required

from app.decorators import role_required
from app.forms.users.role import UpdateUserRoleForm
from app.services.user import UserService

users = Blueprint("users", __name__)


@users.route('/', methods=['GET'])
@login_required
@role_required(['Admin'])
@inject
def list_all(user_service: UserService):
    all_users = user_service.get_all()
    user_forms = {}
    for user in all_users:
        form = UpdateUserRoleForm(obj=user)
        form.user_id.data = user.id
        user_forms[user.id] = form
    return render_template('users/users_list.html', users=all_users, form=user_forms)


@users.route('/update', methods=['POST'])
@login_required
@role_required(['Admin'])
@inject
def update(user_service: UserService):
    form = UpdateUserRoleForm(request.form)
    if form.validate_on_submit():
        user_id = form.user_id.data
        role = form.role.data
        user_service.update(user_id, role)
    return redirect(url_for('users.list_all'))
