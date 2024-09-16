from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_injector import inject
from app.forms.auth.login import LoginForm
from app.models.user import User
from app.services.user import UserService

auth = Blueprint("auth", __name__)


@auth.route('/login', methods=['GET', 'POST'])
@inject
def login(user_service: UserService):
    error_message = ""
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if user_service.login(login_form.username.data, login_form.password.data):
            return "Logged in"
        error_message = "Invalid username or password"
    return "login"
    # return render_template('auth/login.html', form=login_form, error_message=error_message)
