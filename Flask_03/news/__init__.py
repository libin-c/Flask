from flask import Blueprint
from flask_restful import Api
from news.articles import ArticleResource

article_bp = Blueprint('article', __name__)

article_api = Api(article_bp)

article_api.add_resource(ArticleResource, '/article')
