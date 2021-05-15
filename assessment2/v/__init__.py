from flask import Flask

# v = Flask(__name__)
from assessment2 import assessment2

v = assessment2
from . import login_page, registration, main, logout



# def v():
#     return None
#
#
# def route(methods=None):
#     if methods is None:
#         methods = ['GET', 'POST']
#     return None
