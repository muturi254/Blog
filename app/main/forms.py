from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import Required, Length, Email, EqualTo

class ContactForm(FlaskForm):
    email = StringField('Email', validators = [Required(), Length(min=5, max=30), Email()])
    subject = StringField('Subject', validators = [Required])
    message = TextAreaField('Message', validators = [Required()])
    submit = SubmitField('Submit')