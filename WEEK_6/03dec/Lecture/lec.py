from flask import Flask, render_template, render_template_string
import json
import flask_wtf
import wtforms
from wtforms.validators import data_required
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(16)


class Form(flask_wtf.FlaskForm):
    name = wtforms.StringField('Full Name', validators=[data_required()])
    Job = wtforms.StringField('Job', validators=[data_required()])
    submit = wtforms.StringField('Submit')


@app.route('/form', methods=['GET', 'POST'])  # if we don't put, the server will not take/accept data
def CompleteForm():
    form = Form()

    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data

        with open('data.json', 'r') as f:
            data = json.load(f)

        try:
            data[category].append(name)
        except KeyError:
            pass

    return render_template('lec.html', data='Hellloooo')

if __name__ == "__main__":
    app.run()
