# EXERCISE 1
from cgitb import html

from flask import Flask, render_template
import datetime as dt

app = Flask(__name__)


@app.route('/greeting')
def greetin():
    hour = str(dt.datetime.now().hour)
    return render_template('greetinH.html', hour=hour)


# if __name__ == '__main__':
#     app.run()


# EXERCISE 2

@app.route('/')
def home():
    disp1 = """
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Market BETA</title>
                <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv
                    -hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16">
            </head>
            <body style="background-color: beige">
                <h1 style="color: red; font-size: 40px; text-align: center;">! WELCOME TO TEST-MARKET !</h1>
                <p style="color: brown; font-size: 20px; text-align: center;"> We hope you'll love the shop!</p><br>
                <a href="http://127.0.0.1:5000/products"><button type="button">Let's see our products!</button></a>
            </body>
            </html>
        """
    return disp1


@app.route('/products')
def products():
    disp2 = """
                <html>
                <head>
                    <meta charset="UTF-8">
                    <title>Market BETA</title>
                    <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv 
                        -hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16">
                </head>
                <body style="background-color: beige">
                    <h1 style="color: red; font-size: 40px; text-align: center;">! LIST OF PRODUCTS !</h1>
                    <p style="color: brown; font-size: 30px; text-align: center;">Take into consideration that that's a 
                    BETA TEST, so we don't have many products</p><br>
                
                    <ul style="font-size: 20px;">
                        <li style:"list-style: none; color: grey;"><strong>PHONES</strong></li>
                        <li><a href="http://127.0.0.1:5000/products/SamGalS7">Samsung Galaxy S7</a></li>
                        <li><a href="http://127.0.0.1:5000/products/SamGalS10">Samsung Galaxy S10</a></li>
                        <li><a href="http://127.0.0.1:5000/products/IphoneX">Iphone X</a></li>
                        <li><a href="http://127.0.0.1:5000/products/KosherPhone">Kosher Phone</a></li>                 
                    </ul>
                    <ul style="font-size: 20px;">
                        <li style:"list-style: none; color: grey"><strong>COMPUTERS</strong></li>
                        <li><a href="http://127.0.0.1:5000/products/ASRGIC7GTX1050">ASUS Strix Republic of Gamers Intel 
                        Core i7 GTX1050</a></li>
                        <li><a href="http://127.0.0.1:5000/products/AA7IC7GTX750M">ACER Aspire7 intel Core i7 
                        GTX750m</a></li>
                        <li><a href="http://127.0.0.1:5000/products/Macbook">Mac book</a></li>
                        <li><a href="http://127.0.0.1:5000/products/DIC5">DELL Intel Core i5</a></li>                 
                    </ul>
                </body>
                </html>
            """
    return disp2


@app.route('/products/SamGalS7')
def first_select():
    disp21 = """<html>
               <head>
                    <meta charset="UTF-8">
                    <title>Market BETA</title>
                    <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv 
                        -hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16">
               </head>
               <body style="background-color: beige">
               <h1 style="color: red; font-size: 40px; text-align: center;">! DETAIL OF THE SELECTION !</h1>
               <p style="color: brown; font-size: 30px; text-align: center;"> take into consideration that that's a
                BETA TEST. <a href="http://127.0.0.1:5000/products">Come Back to the Products List</a></p><br>
                
                <h4>Samsung Galaxy S7</h4>
                <ul style:"list-style: none;">
                    <li>Color: Black</li>
                    <li>Cost: 1000 ₪</li>
                    <li>Available</li>
                </ul
            </body>
            </html>
        """
    return disp21


@app.route('/products/SamGalS10')
def second_select():
    disp22 = """<html>
               <head>
                    <meta charset="UTF-8">
                    <title>Market BETA</title>
                    <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv 
                        -hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16">
               </head>
               <body style="background-color: beige">
               <h1 style="color: red; font-size: 40px; text-align: center;">! DETAIL OF THE SELECTION !</h1>
               <p style="color: brown; font-size: 30px; text-align: center;"> take into consideration that that's a
                BETA TEST. <a href="http://127.0.0.1:5000/products">Come Back to the Products List</a></p><br>

                <h4>Samsung Galaxy S10</h4>
                <ul style:"list-style: none;">
                    <li>Color: Dark Blue</li>
                    <li>Cost: 3000 ₪</li>
                    <li>Available</li>
                </ul
            </body>
            </html>
        """
    return disp22


@app.route('/products/IphoneX')
def third_select():
    disp23 = """
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Market BETA</title>
                <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv 
                    -hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16">
            </head>
               <body style="background-color: beige">
               <h1 style="color: red; font-size: 40px; text-align: center;">! DETAIL OF THE SELECTION !</h1>
               <p style="color: brown; font-size: 30px; text-align: center;"> take into consideration that that's a
                BETA TEST. <a href="http://127.0.0.1:5000/products">Come Back to the Products List</a></p><br>

                <h4>Iphone X</h4>
                <ul style:"list-style: none;">
                    <li>Color: Black</li>
                    <li>Cost: 4000 ₪</li>
                    <li>Available</li>
                </ul
            </body>
            </html>
        """
    return disp23


@app.route('/products/KosherPhone')
def fourth_select():
    disp24 = """
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Market BETA</title>
                <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv 
                    -hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16">
            </head>
            <body style="background-color: beige">
               <h1 style="color: red; font-size: 40px; text-align: center;">! DETAIL OF THE SELECTION !</h1>
               <p style="color: brown; font-size: 30px; text-align: center;"> take into consideration that that's a
                BETA TEST. <a href="http://127.0.0.1:5000/products">Come Back to the Products List</a></p><br>

                <h4>Kosher Phone</h4>
                <ul style:"list-style: none;">
                    <li>Color: Black</li>
                    <li>Cost: 150 ₪</li>
                    <li>Available</li>
                </ul
            </body>
            </html>
        """
    return disp24


@app.route('/products/ASRGIC7GTX1050')
def fifth_select():
    disp25 = """
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Market BETA</title>
                <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv 
                    -hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16">
            </head>
            <body style="background-color: beige">
               <h1 style="color: red; font-size: 40px; text-align: center;">! DETAIL OF THE SELECTION !</h1>
               <p style="color: brown; font-size: 30px; text-align: center;"> take into consideration that that's a
                BETA TEST. <a href="http://127.0.0.1:5000/products">Come Back to the Products List</a></p><br>

                <h4>ASUS Strix Republic of Gamers Intel Core i7 GTX1050</h4>
                <ul style:"list-style: none;">
                    <li>Color: Black & Red</li>
                    <li>Cost: 6000 ₪</li>
                    <li>Available</li>
                </ul
            </body>
            </html>
        """
    return disp25


@app.route('/products/AA7IC7GTX750M')
def sixth_select():
    disp26 = """
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Market BETA</title>
                <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv 
                    -hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16">
            </head>
            <body style="background-color: beige">
               <h1 style="color: red; font-size: 40px; text-align: center;">! DETAIL OF THE SELECTION !</h1>
               <p style="color: brown; font-size: 30px; text-align: center;"> take into consideration that that's a
                BETA TEST. <a href="http://127.0.0.1:5000/products">Come Back to the Products List</a></p><br>

                <h4>ACER Aspire7 intel Core i7 GTX750m</h4>
                <ul style:"list-style: none;">
                    <li>Color: Black & Grey</li>
                    <li>Cost: 2500 ₪</li>
                    <li>Available</li>
                </ul
            </body>
            </html>
        """
    return disp26


@app.route('/products/Macbook')
def seventh_select():
    disp27 = """
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Market BETA</title>
                <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv 
                    -hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16">
            </head>
            <body style="background-color: beige">
               <h1 style="color: red; font-size: 40px; text-align: center;">! DETAIL OF THE SELECTION !</h1>
               <p style="color: brown; font-size: 30px; text-align: center;"> take into consideration that that's a
                BETA TEST. <a href="http://127.0.0.1:5000/products">Come Back to the Products List</a></p><br>

                <h4>Mac Book</h4>
                <ul style:"list-style: none;">
                    <li>Color: Grey % White</li>
                    <li>Cost: 3500 ₪</li>
                    <li>Unavailable</li>
                </ul
            </body>
            </html>
        """
    return disp27


@app.route('/products/DIC5')
def eight_select():
    disp28 = """
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Market BETA</title>
                <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv 
                    -hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16">
            </head>
            <body style="background-color: beige">
               <h1 style="color: red; font-size: 40px; text-align: center;">! DETAIL OF THE SELECTION !</h1>
               <p style="color: brown; font-size: 30px; text-align: center;"> take into consideration that that's a
                BETA TEST. <a href="http://127.0.0.1:5000/products">Come Back to the Products List</a></p><br>

                <h4>DELL Intel Core i5</h4>
                <ul style:"list-style: none;">
                    <li>Color: Black</li>
                    <li>Cost: 1500 ₪</li>
                    <li>Unavailable</li>
                </ul
            </body>
            </html>
        """
    return disp28





if __name__ == '__main__':
    app.run()
