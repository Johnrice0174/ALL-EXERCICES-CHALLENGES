# EXERCISE 1

# from flask import Flask
# import os
# import binascii
# from flask import app
# import wtforms
#
# app = Flask(__name__)
#
# key = binascii.hexlify(os.urandom(256))
# app.config['BLS_KEY'] = key
#
# print(key)

# EXERCISE 2
from flask import Flask
from flask import app
import cgi

app = Flask(__name__)


@app.route('/')
def form():
    html = """<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>My Form</title>
        <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv
                    -hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16">
    <link href="https://fonts.googleapis.com/css?family=Bree+Serif&display=swap" rel="stylesheet">
    </head>
    <body style="background-color: lightblue;">
    
        <div class="pres" style="background-color: salmon; padding: 5px;">
            <h1 style="text-align: center; color: blue; font-family: 'Bree Serif', serif; margin-top: 0px;">MARKET'S FORM EXERCISE 2</h1>
            <div class="nav" style="display: flex; justify-content: inline-block;">
                <form method="post" action="result.py" style="diplay: flex; justify-content: center;">
                    <p><input type="text" name="name" placeholder="Your product's name...">
                    <input type="text" name="price" placeholder="Price"><label style="font-weight: bold;">₪</label>
                    <select>
                        <option>CATEGORY</option>
                        <option>Literature</option>
                        <option>High Tech</option>
                        <option>Home Appliance</option>
                        <option>Clothing</option>
                        <option>Other</option>
                    </select>
                    <select>
                        <option>STOCK</option>
                        <option>10</option>
                        <option>20</option>
                        <option>30</option>
                        <option>50</option>
                        <option>Full Stock</option>
                    </select>
                    <input type="submit" value="Send"></p>
                </form>
                <ul style="list-style: none; display: flex; justify-content: inline-block; font-size: 20px; font-weight: bold; margin: 10px 5px 0px 600px;">
                    <li><a href="#">About us  |  </a></li>
                    <li><a href="#">Order  |  </a></li>
                    <li><a href="#">Contact  |</a></li>     
                </ul>
            </div>
        </div>
    </body>
    </html>
    """
    return html
# background-image: url("https://kids.nationalgeographic.com/content/dam/kidsea/kids-core-objects/
#     backgrounds/youareleaving_bkgrnd.adapt.1900.1.jpg")

if __name__ == '__main__':
    app.run()
