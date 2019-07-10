from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)


class HelloWordResource(Resource):
    """
    helloword 的类视图

    """

    def get(self):
        return 'Hello Word'

    def post(self):
        return {'msg': 'Hello world'}


api.add_resource(HelloWordResource, '/', endpoint='HelloWorld')

if __name__ == '__main__':
    app.run()
