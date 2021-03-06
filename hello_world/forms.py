# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from wtforms.validators import Length, Regexp
from hello_world.models import User


class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField(u'Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj')


class RegistrationForm(FlaskForm):
    username = StringField(
        'Login',
        validators=[DataRequired(),
                    Length(message=u'Długość loginu: między 4 a 24 znaki',
                           min=4, max=24),
                    Regexp(regex=r'^\w+$',
                           message='Tylko litery A-Z i cyfry')])
    email = StringField('Email', validators=[DataRequired(),
                        Email(message=u'Wpisz prawidłowy adres')])
    password = PasswordField(u'Hasło', validators=[DataRequired()])
    password2 = PasswordField(
        u'Powtórz hasło',
        validators=[DataRequired(),
                    EqualTo('password', message=u'Hasła nie są zgodne')])
    submit = SubmitField('Zarejestruj')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(u'Użyj innego loginu')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(u'Użyj innego adresu email')


class EditProfileForm(FlaskForm):
    aboutme = TextAreaField('O mnie', validators=[Length(min=0, max=140)])
    submit = SubmitField('Zapisz')
    back = SubmitField('Cofnij')


class PostForm(FlaskForm):
    post = TextAreaField('Co u Ciebie?', validators=[
        DataRequired(), Length(min=1, max=400)])
    submit = SubmitField(u'Podziel się')


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(
        u'Twój email',
        validators=[DataRequired(),
                    Email(message=u'Wpisz prawidłowy adres')])
    submit = SubmitField(u'Wyślij')


class ResetPasswordForm(FlaskForm):
    password = PasswordField(u'Hasło', validators=[DataRequired()])
    password2 = PasswordField(
        u'Powtórz hasło',
        validators=[DataRequired(),
                    EqualTo('password', message=u'Hasła nie są zgodne')])
    submit = SubmitField(u'Potwierdź')
