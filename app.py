from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('01_cover.html')


@app.route("/vida")
def life():
    return render_template('10_life.html')


@app.route("/proyectos")
def projects():
    return render_template('20_projects.html')


@app.route("/marca")
def brand():
    return render_template('30_brand.html')


@app.route("/Contacto")
def contact():
    return render_template('40_contact.html')


@app.route("/blog")
def blog():
    return render_template('90_blog.html')
