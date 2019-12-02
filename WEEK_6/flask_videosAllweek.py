# micro framework of python with small libraries
# (django is a massive framework)

# on cmd
# mkdir myproject
# cd myproject
# mac: python -m venv foldername // win: py -3 -m venv foldername
#
# venv\Scripts\active # active the venv

# pip --version // pip3 --version
#
# pip install flask
#
# WARNING: You are using pip version 19.2.3, however version 19.3.1 is available.
# You should consider upgrading via the 'python -m pip install --upgrade pip' command.

# ---- TEMPLATES ----

from flask import Flask, render_template_string

# il s'agit d'importer flask APRÈS INSTALLATION sur chaque Projet!!
app = Flask(__name__)
print(__name__)


@app.route('/')
# il s'agit de chemin d'accès, les etapes post-lien (.../blog/perso...)
def hello_world():
    html = f"""
            <html>
            
                <head>
                    <title>Home Page</title>
                    <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv
                    -hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16"> 
                </head>
                
                <body>
                    <h1>HELLO !!!!!!</h1>
                    <a href="http://127.0.0.1:5000/blog">My Blog</a>
                </body>
            
            </html>
    """
    return html


@app.route('/blog')
def blogpage():
    html = f"""
            <html>

                <head>
                    <title>My Blog</title>
                    <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv
                    -hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16"> 
                </head>

                <body>
                    <h1>MY BLOG</h1>
                    <p>My Name is Adrian John Kugler Dury (alias John Rice)</p>
                    <a href="http://127.0.0.1:5000/">Homepage</a><br>
                    <a href="http://127.0.0.1:5000/blog/2020/cats">CAT'S NEWS</a>
                </body>

            </html>
    """
    return html


@app.route('/blog/2020/cats')
def blog2():
    html = f"""
            <html>

                <head>
                    <title>My Blog</title>
                    <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv
                    -hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16"> 
                </head>

                <body>
                    <h1>CAT'S NEWS</h1>
                    <p>In 2020, there will be hundred thousands of cats in the israeli's streets</p>
                    <a href="http://127.0.0.1:5000/">Homepage</a><br>
                    <a href="http://127.0.0.1:5000/blog/">My Blog</a>
                </body>

            </html>
    """
    return html


if __name__ == '__main__':
    app.run()

# ---------- F L A S K ----------------
# Flask est la façon simple de faire le LIEN
# entre Python et le web (html, css)

# ----------- URL FOR Flask -------------
# permet de façon plus Flask de faire le liens entre les diffférents @app.route (au lieu de <a href=''></a>
# from flask import url_for
# code.... @app.route ....
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Rice'))

# ---------------------------------------


