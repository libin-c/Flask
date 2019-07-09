from  flask import Blueprint,current_app

user_bp = Blueprint('user',__name__)

@user_bp.route('/user')
def users():
    return '{}'.format(current_app.redis_client)