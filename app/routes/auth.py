from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_injector import inject
from flask_login import login_required

from app.models.user import User
from app.services.user import UserService
from app.forms.auth.login import LoginForm
from app.forms.auth.signup import SignupForm

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


@auth.route('/signup', methods=['GET', 'POST'])
def signup(user_service: UserService):
    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        if not user_service.get_by_username(username=signup_form.username.data) and not user_service.get_by_email(
                email=signup_form.email.data):
            user_service.signup(
                signup_form.username.data,
                signup_form.email.data,
                signup_form.password.data
            )
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', form=signup_form)


@auth.route('/logout')
@login_required
@inject
def logout(user_service: UserService):
    user_service.logout()
    return redirect(url_for('auth.login'))
