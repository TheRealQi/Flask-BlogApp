from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, length, Regexp


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=4, max=20)])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), length(min=6), Regexp(r'^(?=.*[A-Z])(?=.*[\W_]).{6,}$')])
    submit = SubmitField('Login')
