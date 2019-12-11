from flask import Flask, render_template
# render_template (c kan on a un fichier template donc exterieur)
# render_template_string (c kan on fait le html directement dans le fichier python)
import wtforms
import flask_wtf
import random

site = Flask(__name__)
site.config['SECRET_KEY'] = random._urandom(256)
print(random._urandom(256))

# creation des input
class Form(flask_wtf.FlaskForm):
    name = wtforms.StringField('Name: ')
    price = wtforms.IntegerField('Price in ₪ : ')
    category = wtforms.SelectField(u'CATEGORY',
                                   choices=[('clt', 'clothing'), ('hgtc', 'High-Tech'), ('hap', 'Home Appliance'),
                                            ('fd', 'Food')])
    stock = wtforms.RadioField('STOCK',
                               choices=[(10, 'ten available'), (20, 'twenty available'), (50, 'fifty available')])
    submit = wtforms.SubmitField('Add')


@site.route("/")
def addf():
    pizza = Form()
    css = open('static/style.css', 'r').read()
    return render_template('index.html', form=pizza, csss=css)


if __name__ == '__main__':
    site.run(debug=True)
