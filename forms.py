from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo, Regexp
from wtforms.widgets import TextArea

class SignupForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    username = StringField('Username', validators=[InputRequired(),
                            Length(min=3, max=15),
                            Regexp('^[A-Za-z][A-Za-z0-9_]*$', 0,
                            'Username must start with a letter and can only contain letters, numbers and underscores.')])
    password = PasswordField('Password', validators=[InputRequired(),
                            Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(),
                            EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(),
                            Length(min=6, max=20)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    message = StringField('Message', validators=[InputRequired()], widget=TextArea())
    submit = SubmitField('Submit')
