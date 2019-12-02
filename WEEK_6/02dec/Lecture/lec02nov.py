import json

data = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    loaded_data = json.load(f)

print(loaded_data)
print(type(loaded_data))
print(data == loaded_data)

# ----------------------------------------

from flask import Flask, render_template, render_template_string

app = Flask(__name__)


@app.route('/realm/<realm>')
def realm_index(realm):
    return render_template('realm.html', realm=realm)


@app.route('/particles')
def particles_view():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return render_template('particles.html', particles=data)


if __name__ == '__main__':
    app.run()

# ------------------------------------------------

