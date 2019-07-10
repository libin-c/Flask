from flask_restful import Resource


class ArticleResource(Resource):

    def get(self):
        return 'Article Resource'

    def post(self):
        return {'data': 'Article Resource'}
