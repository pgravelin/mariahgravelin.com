from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators

class ContactForm(Form):
    name = TextField("Name",  [validators.Required()])
    email = TextField("Email",  [validators.Required(), validators.Email("Please enter your email address.")])
    subject = TextField("Subject",  [validators.Required()])
    message = TextAreaField("Message",  [validators.Required()])