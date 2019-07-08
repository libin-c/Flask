# app = Flask(__name__)相当于django—admin
# Blueprint 相当于startapp  也就是子应用

from flask import  Blueprint

user_bp=Blueprint('user',__name__)

@user_bp.route('/')
def user_project():
    return 'user_project'

