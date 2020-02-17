from flask import Flask, render_template_string

app = Flask(__name__)


# @app.route('/')
# # if the client request is / i call func that return html
# def index():
#     html = 'השלום עליכם ורחמנות האל בברכתו'
#     return html
#
# if __name__ == '__main__':
#     app.run() #make the website, run it

# ---------------------------

# @app.route('/home/<your_name>')
# # if the client request is / i call func that return html
# def personal_index(your_name):
#     html = f"""
#     <html>
#         <head>
#             <title>YourIndex</title>
#             <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv-hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16">
#         </head>
#         <body>
#             <h1> La Paix du Seigneur soit sur vous {your_name}</h1>
#             <h1>שלום עליכם ורחמנות האל וברכתו</h1>
#         </body>
#     </html>
#     """
#     return html


# @app.route('/home2/<your_name>')
# def template_index(your_name):
#     html = """
#     <html>
#         <head>
#             <title>YourIndex</title>
#             <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5y4PNw72yv-hge_rNWq3ap3Tt1Ay5uvd8nGBP_v6JiWtprz_S&s" type="image/gif" sizes="16x16">
#         </head>
#         <body>
#             <h1> La Paix du Seigneur soit sur vous {{ name }}</h1>
#             <h1>{{ name }} שלום עליכם ורחמנות האל וברכתו</h1>
#         </body>
#     </html>
#     """
#     return render_template_string(html, name=your_name)

# ----------------------------------

@app.route('/home3/<your_name>')
def template_index(your_name):
    with open('name.jinja', encoding='utf8') as f:
        html = f.read()
    length = len(your_name)
    return render_template_string(html, name=your_name, length=length)


if __name__ == '__main__':
    app.run()  # make the website, run it

# -------- INTO HTML FILE ----------
# {{ variable }}
# {% statement %} #if, for....
# {# comment #}
