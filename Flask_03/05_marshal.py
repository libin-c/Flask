from flask import Flask
from flask_restful import Resource, Api, marshal, fields

# marshal 对复用性高的字段可以选择使用
# 相当于Django中的serializer

app = Flask(__name__)

api = Api(app)


class User(object):
    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age


user_fields = {
    'user_id': fields.Integer,
    'name': fields.String
}


class HelloWordResource(Resource):

    def get(self):
        # user = Users.objects.get()
        user = User(123, 'python', 18)

        # 需求： 将对象转换为字典   序列化
        # user_dict = marshal(user, user_fields)
        #
        # # return {'user_id': 123, 'name':'python' }
        # return user_dict

        user_dict = marshal(user, user_fields, envelope='data')

        # return {'data':{'user_id': 123, 'name':'python' }}
        return user_dict

        # user_dict = {
        #     'user_id': user.user_id,
        #     'name': user.name
        # }
        # return user_dict


api.add_resource(HelloWordResource, '/')

if __name__ == '__main__':
    app.run()
