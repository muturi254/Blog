from flask-wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtform.validator import Required

class ContactForm(FlaskForm):
    Username = StringField('Username', [validator= Required()])
    email = StringField('email', [validator= Required()])
    comment = TextAreaField('Textarea', [validator.length(max=10, max=255)]) 