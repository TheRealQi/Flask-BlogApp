from flask_wtf import FlaskForm
from pyexpat.errors import messages
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, length, Regexp


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   length(min=4, message="Username must contain atleast 4 characters")])
    email = EmailField('Email', validators=[DataRequired(message="Please provide an email address!"),
                                            Regexp(r'^[\w\.-]+@([\w-]+\.)+[\w-]{2,}$',
                                                   message="Invalid email address")])
    password = PasswordField('Password',
                             validators=[DataRequired(message="Please fill this field!"),
                                         length(min=6, message="Password must contain atleast 6 characters"),
                                         Regexp(r'^(?=.*[A-Z])(?=.*[\W_]).{6,}$',
                                                message="Password must contain atleast 1 uppercase letter and 1 special character")])
    submit = SubmitField('Login')
