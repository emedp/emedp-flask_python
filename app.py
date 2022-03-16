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


@app.route("/atenea")
def atenea():
    return render_template('20_atenea.html')

@app.route("/emedpware")
def brand():
    return render_template('30_brand.html')


@app.route("/rrss")
def rrss():
    return render_template('40_rrss.html')


@app.route("/privacy")
def privacy():
    return render_template('98_privacy.html')


@app.route("/tos")
def tos():
    return render_template('99_terms_of_service.html')
