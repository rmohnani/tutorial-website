from app import app
from flask import escape, redirect, url_for

@app.route('/')
def hello():
    return 'Hello World!'

# @app.route('/<string:user>')
# def user(user):
#     if user == 'rohit':
#         return 'Hello Administrator %s' % escape(user)
#     else:
#         return 'Hello %s!' % escape(user)

# @app.route('/<int:numb>')
# def say(numb):
#     return 'You are number %d' % numb

@app.route('/student/<string:student>')
def hello_student(student):
    return 'Hello student %s!' % escape(student)

@app.route('/teacher/<string:teacher>')
def hello_teacher(teacher):
    return 'Hello teacher %s' % escape(teacher)

@app.route('/user/<string:name>')
def hello_u(name):
    if name == 'rohit':
        return redirect(url_for('hello_teacher', teacher = name))
    else:
        return redirect(url_for('hello_student', student = name))