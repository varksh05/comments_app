from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class CommentForm(FlaskForm):
    comment = TextAreaField('Address', validators=[DataRequired(), Length(min=1, max=120)])
    submit = SubmitField('Comment')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=45)])
    secret = StringField('reset', validators=[DataRequired(), Length(min=1, max=45)])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email',  validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=45)])
    submit = SubmitField('Login')


class ResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    secret = StringField('reset', validators=[DataRequired(), Length(min=1, max=45)])
    submit = SubmitField('Reset')
