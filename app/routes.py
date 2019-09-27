from app import app
from flask import escape, redirect, url_for, render_template, flash, request
from forms import SignupForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/signup', methods = ['GET', 'POST'])
def tutor_signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'Tutor {form.first_name.data}, {form.last_name.data}, {form.school_email.data}, {form.grade_choices.data}, {form.subject.data} is now signed up')
        return redirect(url_for('home_page'))
    
    else:
        flash(f'Tutor {form.first_name.data} is not signed up', 'failure')
        return render_template('signup.html', title = 'Sign Up', form = form)
    

@app.route('/request')
def tutor_request():
    return render_template('request.html')

@app.route('/teacher_student_request')
def teacher_student_request():
    return render_template('teacher_student_request.html')

@app.route('/teacher_admin')
def teacher_admin():
    return render_template('teacher_admin.html')

# @app.route('/<string:user>')
# def user(user):
#     if user == 'rohit':
#         return 'Hello Administrator %s' % escape(user)
#     else:
#         return 'Hello %s!' % escape(user)

# @app.route('/<int:numb>')
# def say(numb):
#     return 'You are number %d' % numb

# @app.route('/student/<string:student>')
# def hello_student(student):
#     return 'Hello student %s!' % escape(student)

# @app.route('/teacher/<string:teacher>')
# def hello_teacher(teacher):
#     return 'Hello teacher %s' % escape(teacher)

# @app.route('/user/<string:name>')
# def hello_u(name):
#     if name == 'rohit':
#         return redirect(url_for('hello_teacher', teacher = name))
#     else:
#         return redirect(url_for('hello_student', student = name))