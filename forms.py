from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms import SelectField


class RegisterForm(Form):
    firstname = TextField(
        'Username', validators=[DataRequired(), Length(min=2, max=25)]
    )

    lastname = TextField(
        'Name', validators=[DataRequired(), Length(min=2, max=25)]
    )

    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )

    address = TextField(
        'address', validators=[DataRequired(), Length(min=2, max=150)]
    )
    phonenumber = TextField(
        'phonenumber', validators=[DataRequired(), Length(min=10, max=13)]
    )
    group = TextField(
        'group', validators=[DataRequired(), Length(min=2, max=40)]
    )

class LoginForm(Form):
    name = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])

class SearchForm(Form):
    search = SelectField(
        'Search Type', choices=[
            ('group', 'group')
            ])
    search2 = SelectField(
        'Search Type', choices=[
            ('person', 'person-group')
            ])
    search3 = SelectField(
        'Search Type', choices=[
            ('firstname', 'firstname')
            ])
    search4 = SelectField(
        'Search Type', choices=[
            ('lastname', 'lastname')
            ])
    search5 = SelectField(
        'Search Type', choices=[
            ('firstname_lastname', 'firstname_lastname')
            ])
    value = TextField(
        'value', validators=[DataRequired(), Length(min=2, max=25)]
    )
    value2 = TextField(
        'value2', validators=[DataRequired(), Length(min=2, max=25)]
    )

class AddGroupForm(Form):
    search = SelectField(
        'Search Type', choices=[
            ('group', 'group')
            ])

    value = TextField(
        'GroupName', validators=[DataRequired(), Length(min=2, max=25)]
    )
