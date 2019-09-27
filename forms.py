from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, Optional

class SignupForm(FlaskForm):
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name =  StringField('Last Name', validators = [DataRequired()])
    school_email = StringField('GIS Email', validators = [Email()])
    grade_choices = SelectField(u'Form', coerce = str, choices = [('1', 'Form 1'), ('2', 'Form 2'), ('3', 'Form 3'), ('4', 'Form 4'), ('5', 'Form 5'), ('L6', 'Lower 6'), ('U6', 'Upper 6')])
    subject_choices = SelectMultipleField(u'Subject', coerce = str, choices = [('AM', 'Additional Mathematics'), ('PHY', 'Physics'), ('LIT', 'Literature')])
    time = SelectMultipleField(u'Times Available', choices = [('M12', '1st and 2nd'), ('M34', '3rd and 4th'), ('M56', '5th and 6th')])
    submit = SubmitField('Sign up')
   
