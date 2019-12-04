from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, ValidationError
from wtforms.widgets import TextArea

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = StringField('Message', validators=[DataRequired()], widget=TextArea())
    submit = SubmitField('Submit')


class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(),
                            Length(min=3, max=15),
                            Regexp('^[A-Za-z][A-Za-z0-9_]*$', 0,
                            'Username must start with a letter and can only contain letters, numbers and underscores.')])
    password = PasswordField('Password', validators=[DataRequired(),
                            Length(min=6, max=36)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
                            EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(f'Username {username} is already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(f'Email {email} is already taken.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                            Length(min=6, max=20)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')
