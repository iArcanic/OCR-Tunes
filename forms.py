from flask_wtf import FlaskForm
from wtforms import (StringField,
                     SubmitField,
                     PasswordField,
                     DateField,
                     SelectField)
from wtforms.validators import (DataRequired,
                                EqualTo)


class RegisterForm(FlaskForm):
    """Sign up for a OCRTunes account."""
    first_name = StringField('First Name', [DataRequired()])
    last_name = StringField('Last Name', [DataRequired()])
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired(message="Please enter a password.")])
    confirmPassword = PasswordField('Repeat Password', [EqualTo(password, message='Passwords must match.')])
    genre = SelectField(
        'Genre', [DataRequired()],
        choices=[('Pop', 'pop'),
                ('Hip-Hop', 'rap'),
                ('Rock/Heavy Metal', 'rock'),
                ('Jazz', 'jazz')])
    favourite_artist = StringField('Favourite Artist', [DataRequired()])
    birthday = DateField('Your Date of Birth')
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """Sign In."""
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired(message="Please enter a password.")])
    submit = SubmitField('Login')