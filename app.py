from flask import Flask, render_template, url_for, request, flash, redirect
from forms.forms import ContactForm
from urllib.parse import urlparse, urlunparse
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

@app.before_request
def redirect():
    urlparts = urlparse(request.url)
    if urlparts.netloc == 'www.mariahgravelin.heroku.com:80':
        urlparts_list = list(urlparts)
        urlparts_list[1] = 'www.mariahgravelin.com:80'
        return redirect(urlunparse(urlparts_list), code=301)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio/audition")
def audition():
    return render_template("audition.html")

@app.route("/portfolio/dance")
def dance():
    return render_template("dance.html")

@app.route("/portfolio/interior_design")
def interior_design():
    return render_template("interior_design.html")

@app.route("/portfolio/portrait")
def portrait():
    return render_template("portrait.html")

@app.route("/portfolio/street")
def street():
    return render_template("street.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)