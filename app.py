from flask import Flask, render_template, url_for, request, flash, redirect
from forms.forms import ContactForm

app = Flask(__name__)

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
        if not form.validate():
            flash("All fields are required")
            return render_template("contact.html", form=form)
        else:
            return "Form posted."
    
    if request.method == "GET":
        return render_template("contact.html", form=form)
    
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)