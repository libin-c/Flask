from flask import Flask, current_app
from flask_restful import Api, Resource
from flask import make_response, current_app
from flask_restful.utils import PY3
from json import dumps

# 创建flask对象
app = Flask(__name__)

# 创建restful扩展提供的api对象
api = Api(app)


@api.representation('application/json')
def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""

    # 是flask-restful提供的原始处理视图输出结果的方法
    #     # 传入参数说明
    #     # data -> 视图返回的字典数据
    #     # code -> 视图返回的状态码数据
    #     # headers -> 视图返回的响应头数据
    #
    #     # 需求分析
    #     # 视图可能返回 data  {'user_id': , 'name': }
    #
    #     # 只对视图正确输出做处理，对于视图返回的错误信息，不做处理
    if 'message' not in data:
        data = {
            'message': 'ok',
            'data': data
        }

    settings = current_app.config.get('RESTFUL_JSON', {})

    # If we're in debug mode, and the indent is not set, we set it to a
    # reasonable value here.  Note that this won't override any existing value
    # that was set.  We also set the "sort_keys" value.
    if current_app.debug:
        settings.setdefault('indent', 4)
        settings.setdefault('sort_keys', not PY3)

    # always end the json dumps with a new line
    # see https://github.com/mitsuhiko/flask/pull/1262
    dumped = dumps(data, **settings) + "\n"

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp

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
