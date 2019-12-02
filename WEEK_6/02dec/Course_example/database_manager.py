import json


def create_database(dst_file='my_file.json'):
    data = [
        {
            'name': 'iphone 9',
            'price': 799,
            'remains': True
        },

        {
            'name': 'Macbook Pro',
            'price': 4799,
            'remains': False
        },

        {
            'name': 'Apple Watch',
            'price': 10799,
            'remains': True
        },

        {
            'name': 'Apple stand pro',
            'price': 99999,
            'remains': True
        },
    ]
    with open(dst_file, 'w') as file_obj:
        json.dump(data, file_obj)


def load_database(src_file='my_file.json'):
    with open(src_file, 'r') as file_obj:
        data = json.load(file_obj)
    return data


# a file my_file.json was automatically created and contains our database (dictionary)

# ------------------------------------------------------------------------

import flask,
import database_manager  # this is our module

app = flask.Flask(__name__)
database_manager.create_database()


@app.route("/")
@app.route("/products")
def products_page():

    data = database_manager.load_database()
    template = open('my_template.jinja', 'r').read()

    return flask.render_template_string(template_file, products=data)


app.run(debug=True)
