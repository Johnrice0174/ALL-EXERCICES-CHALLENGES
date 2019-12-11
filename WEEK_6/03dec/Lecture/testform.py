import flask_wtf
import wtforms
from wtforms.validators import data_required


class Form(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name", validators=[data_required()])
    password = wtforms.PasswordField("Password", validators=[data_required()])
    bio = wtforms.StringField("Bio")
    submit = wtforms.SubmitField("Submit")


my_form = Form()

form_template = """
<form method="POST">
{{ form.hidden_tag() }}

{{ form.username.label }}
{{ form.username(size=32) }}

{{ form.password.label }}
{{ form.password(size=32) }}

{{ form.bio.label }}
{{ form.bio(size=240) }}

{{ form.submit() }}
</form>
"""
