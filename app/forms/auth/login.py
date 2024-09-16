from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, Regexp

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), length(min=6), Regexp(r'^(?=.*[A-Z])(?=.*[\W_]).{6,}$')])
    submit = SubmitField('Login')