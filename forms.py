from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email

class SignupForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name =  StringField('Last Name', validators = [DataRequired()])
    school_email = StringField('GIS Email', validators = [Email()])
    grade = SelectField(u'Form', choices = [('1', 'Form 1'), ('2', 'Form 2'), ('3', 'Form 3'), ('4', 'Form 4'), ('5', 'Form 5'), ('L6', 'Lower 6'), ('U6', 'Upper 6')])
    # subject = SelectMultipleField(u'Subject', choices = [('AM', 'Additional Mathematics'), ('PHY', 'Physics'), ('LIT', 'Literature')])
    submit = SubmitField('Sign up')

