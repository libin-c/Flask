from flask import Blueprint
from flask_restful import  Api,Resource

user_bp = Blueprint('user', __name__)

user_api = Api(user_bp)

class UserBlueprint(Resource):
    def get(self):
        return 'User Blueprint'
    def post(self):
        return {'data':'login data'}


user_api.add_resource(UserBlueprint,'/users')
