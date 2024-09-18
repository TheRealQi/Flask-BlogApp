from flask import Blueprint, render_template

errors = Blueprint("errors", __name__)

@errors.route('/')
def not_authorised():
    return render_template('errors/not_authorised.html')
