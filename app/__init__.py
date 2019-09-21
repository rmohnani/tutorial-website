from flask import Flask
from config import Config

thing = Flask(__name__)
thing.config.from_object(Config)

from app import routes