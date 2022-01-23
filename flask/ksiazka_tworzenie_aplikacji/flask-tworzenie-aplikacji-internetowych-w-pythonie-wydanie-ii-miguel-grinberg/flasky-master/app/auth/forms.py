from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    remember_me = BooleanField('Zapamiętaj mnie')
    submit = SubmitField('Zaloguj')


class RegistrationForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Nazwa użytkownika', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    password = PasswordField('Hasło', validators=[
        DataRequired(), EqualTo('password2', message='Hasła muszą być identyczne.')])
    password2 = PasswordField('Potwierdź hasło', validators=[DataRequired()])
    submit = SubmitField('Zarejestruj')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Ten adres e-mail jest już zarejestrowany.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Ta nazwa użytkownika jest już używana.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Stare hasło', validators=[DataRequired()])
    password = PasswordField('Nowe hasło', validators=[
        DataRequired(), EqualTo('password2', message='Hasła muszą być identyczne.')])
    password2 = PasswordField('Potwierdź nowe hasło',
                              validators=[DataRequired()])
    submit = SubmitField('Zmień hasło')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Resetuj hasło')


class PasswordResetForm(FlaskForm):
    password = PasswordField('Nowe hasło', validators=[
        DataRequired(), EqualTo('password2', message='Hasła muszą być identyczne')])
    password2 = PasswordField('Potwierdź hasło', validators=[DataRequired()])
    submit = SubmitField('Zmień hasło')


class ChangeEmailForm(FlaskForm):
    email = StringField('Nowy adres e-mail', validators=[DataRequired(), Length(1, 64),
                                                 Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaktualizuj adres e-mail')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Adres e-mail jest już zarejestrowany.')
