from flask_wtf import FlaskForm
from wtforms import SelectField, HiddenField, SubmitField
from wtforms.validators import DataRequired

class UpdateUserRoleForm(FlaskForm):
    user_id = HiddenField('User ID', validators=[DataRequired()])
    role = SelectField('Role', choices=[('Admin', 'Admin'), ('Author', 'Author'), ('Reader', 'Reader')], validators=[DataRequired()])
    submit = SubmitField('Update')
