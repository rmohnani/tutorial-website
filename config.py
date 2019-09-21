import os

class Config(object):
    SECRET_KEY = os.eniron.get('SECRET_KEY') or 'you-will-never-guess'
    