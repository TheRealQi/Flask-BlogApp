from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length
from wtforms.widgets.core import TextArea


class CreatePostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(message="Please enter the post's title"),
                                             length(min=5, message="Title must be atleast 5 characters long")])
    content = TextAreaField("Content", validators=[DataRequired(message="Please enter the post's content"),
                                                   length(min=10,
                                                          message="Content must be atleast 10 characters long")],
                            widget=TextArea())
    submit = SubmitField("Submit")
