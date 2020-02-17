# Exercise 1
# Create a view that displays the actual date.
# from datetime import datetime
#
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# # if the client request is / i call func that return html
# def date():
#     now = str(datetime.now())
#     html = f"<h2 style='color: pink; font-size: 40px; text-align: center'>Today's date: {now}</h2>"
#     return html


#
# if __name__ == '__main__':
#     app.run()  # make the website, run it

# Exercise 3
# Use pip to install flask module.
# To try it, run import flask in a python console.

# mkdir myproject
# cd myproject
# mac: python -m venv foldername // win: py -3 -m venv foldername
#
# forldername\Scripts\activate # active the venv
#
# pip --version // pip3 --version
#
# pip install flask

# Exercise 2
# Choose any function you wrote in the functions chapter and store it
# in a separate file then use import it with the following syntaxes:

# Exercise ُ Easy
# Write a template for your CV, and then CSS it.

from flask import Flask, render_template_string

app = Flask(__name__)


@app.route('/mycv')
# if the client request is / i call func that return html
def personal_index():
    name = 'Adrien Jean Kugler Dury'
    hobbies = "gaming, religions, languages, music, youtube, mythology, history, ..."
    skills = "coding, gaming, languages, general knowledge, military experience, ..."
    strengths = "intelligent, assidu, travailleur, heures-sup, digne de confiance, ambitieux, courage, temeraire, " \
                "serieux, responsable, comprehensif, resiliant, sympathique, drole, sociable, altruiste, ... "
    weakness = "susceptible, pessimiste, nerveux, ..."

    html = f"""
    <html>
        <head>
            <title>My CV (Flask)</title>
            <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv
            -hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16">
        </head>
        <body style="background-color: lightgrey">
            <h1 style="text-align: center; color: red; font-size: 60px; text-decoration: underline;"> HERE IS MY CV
            TEST BY FLASK</h1>
            <div class="pic">
                <img src="https://zupimages.net/up/19/44/9f2y.jpg" alt="Profil picture" height="140" width="140">
            </div>
            <p>
                <label style="font-weight: bold; color: blue; font-size: 20px;">Name: </label>{name}
            </p>
            <p>
                <label style="font-weight: bold; color: blue; font-size: 20px;">Hobbies: </label>{hobbies}
            </p>
            <p>
                <label style="font-weight: bold; color: blue; font-size: 20px;">Skills: </label>{skills}
            </p>
            <p>
                <label style="font-weight: bold; color: blue; font-size: 20px;">Strengths: </label>{strengths}
            </p>
            <p>
                <label style="font-weight: bold; color: blue; font-size: 20px;">Weakness: </label>{weakness}
            </p>
        </body>
    </html>
    """
    return html


if __name__ == '__main__':
    app.run()  # make the website, run it
