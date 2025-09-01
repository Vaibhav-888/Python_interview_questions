from flask import request, jsonify, Flask
from functools import wraps

app = Flask(__name__)

def auth_and_log(f):
    @wraps(f)
    def decorator_function():
        def wrapper():
            return f