from app import app
from flask import escape, redirect, url_for, render_template

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/signup')
def tutor_signup():
    return render_template('signup.html')

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