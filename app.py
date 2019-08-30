from flask import Flask, render_template, url_for, request, flash, redirect
from forms.forms import ContactForm
from flask_mail import Message, Mail

app = Flask(__name__)
mail = Mail(app)

app.config["SECRET_KEY"] = b"p\xe6s\x13\xf9*\xd3X?~\x8c\xd1\x0b+)\xc4\xe2\x82\xf7U,\x9bO1"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "mgravphoto@gmail.com"
app.config["MAIL_PASSWORD"] = "gawjjiyyjuzskwff"
 
mail.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/audition")
def audition():
    return render_template("audition.html")

@app.route("/dance")
def dance():
    return render_template("dance.html")

@app.route("/interior_design")
def interior_design():
    return render_template("interior_design.html")

@app.route("/portrait")
def portrait():
    return render_template("portrait.html")

@app.route("/street")
def street():
    return render_template("street.html")

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
            msgBody= """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            msg = mail.send_message(
                form.subject.data,
                sender="mgravphoto@gmail.com",
                recipients=['pygravelin@gmail.com'],
                body=msgBody
            )
            return render_template('contact.html', success=True)
    
    if request.method == "GET":
        return render_template("contact.html", form=form)
    
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)