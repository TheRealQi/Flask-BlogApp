from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_injector import inject
from flask_login import login_required
from app.services.user import UserService
from app.forms.auth.login import LoginForm
from app.forms.auth.signup import SignupForm

auth = Blueprint("auth", __name__)


@auth.route('/login', methods=['GET', 'POST'])
@inject
def login(user_service: UserService):
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if user_service.login(login_form.username.data, login_form.password.data):
            return redirect(url_for('dashboard.home'))
        else:
            flash("Invalid username or password", "danger")
    return render_template('auth/login.html', form=login_form)


@auth.route('/signup', methods=['GET', 'POST'])
@inject
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
        else:
            if user_service.get_by_username(username=signup_form.username.data) and user_service.get_by_email(
                    email=signup_form.email.data):
                flash("Username and email already exists", "danger")
            elif user_service.get_by_username(username=signup_form.username.data):
                flash("Username already exists", "danger")
            elif user_service.get_by_email(email=signup_form.email.data):
                flash("Email already exists", "danger")

    print(signup_form.errors)
    return render_template('auth/signup.html', form=signup_form)


@auth.route('/logout')
@login_required
@inject
def logout(user_service: UserService):
    user_service.logout()
    return redirect(url_for('auth.login'))
