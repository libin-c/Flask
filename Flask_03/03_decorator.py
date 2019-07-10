from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)


def decorator1(func):
    def wrapper(*args, **kwargs):
        print('decorator1')
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):
    def wrapper(*args, **kwargs):
        print('decorator2')
        return func(*args, **kwargs)

    return wrapper


class HelloWordResource(Resource):
    # 每个请求都加这两个装饰器
    method_decorators = [decorator1, decorator2]

    # 以字典的方式为 每个请求加装饰器
    # method_decorators = {
    #     'get': decorator1,
    #     'post': decorator1, decorator2
    # }

    def get(self):
        return {'data': {'name': 'python', 'age': 18}}

    def post(self):
        return {'msg': 'Hello world'}

    # 最终结果是
    # decorator2(decorator1((get)))
    # 不是
    # @decorator1
    # @decorator2
    # def get()  -> 打印输出 decorator1  decorator2

    # 而是
    # @decorator2
    # @decorator1
    # def get() -> 打印输出 decorator2  decorator1

    # 原理：
    # for dec in decorators:
    #     get_view()
    # get_view()----> decorator1(get_view())---->decorator2(decorator1(get_view()))

api.add_resource(HelloWordResource, '/', endpoint='HelloWorld')

if __name__ == '__main__':
    app.run()
