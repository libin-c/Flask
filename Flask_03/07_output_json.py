from flask import Flask, current_app
from flask_restful import Api, Resource

# 创建flask对象
from output import output_json

app = Flask(__name__)

# 创建restful扩展提供的api对象
api = Api(app)



api.representation('application/json')(output_json)
# 编写视图
class HelloWorldResource(Resource):

    def get(self):
        # 参数检验
        # 自己检验
        # 不合格 return {'message': '错误提示信息'}
        # RequestParser 检验 错误 返回 {'message': 错误提示信息}

        # return {'message': "missing a param."}
        return {'user_id': 12, 'name': 'python'}

api.add_resource(HelloWorldResource, '/')


if __name__ == '__main__':
    app.run()
