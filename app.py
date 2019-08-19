from flask import Flask, render_template, url_for, request, flash, redirect
from forms.forms import ContactForm

app = Flask(__name__)
app.config["SECRET_KEY"] = b'p\xe6s\x13\xf9*\xd3X?~\x8c\xd1\x0b+)\xc4\xe2\x82\xf7U,\x9bO1'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    
    if request.method == "POST":
        if not form.validate_on_submit():
            return render_template("contact.html", form=form)
        else:
            return "Form posted."
    
    if request.method == "GET":
        return render_template("contact.html", form=form)
    
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)