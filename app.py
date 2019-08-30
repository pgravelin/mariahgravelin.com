from flask import Flask, render_template, url_for, request, flash, redirect
from forms.forms import ContactForm

app = Flask(__name__)

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