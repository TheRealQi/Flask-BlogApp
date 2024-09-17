from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_injector import inject

from app.forms.users.role import UpdateUserRoleForm  # Import your form class
from app.services.user import UserService

users = Blueprint("users", __name__)

# List all users and generate forms dynamically for each user
@users.route('/', methods=['GET'])
@inject
def list_all(user_service: UserService):
    all_users = user_service.get_all()
    user_forms = {}
    for user in all_users:
        form = UpdateUserRoleForm(obj=user)
        form.user_id.data = user.id
        user_forms[user.id] = form
    return render_template('users/users_list.html', users=all_users, form=user_forms)


# Update user role
@users.route('/update', methods=['POST'])
@inject
def update(user_service: UserService):
    form = UpdateUserRoleForm(request.form)

    # Validate form submission
    if form.validate_on_submit():
        user_id = form.user_id.data
        role = form.role.data
        user_service.update(user_id, role)
        flash('User role updated successfully!', 'success')
    else:
        flash('Form submission failed. Please try again.', 'error')

    return redirect(url_for('users.list_all'))
