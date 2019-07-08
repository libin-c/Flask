
from flask import Blueprint

news_bp = Blueprint('news', __name__)
comments_bp = Blueprint('comments', __name__)

from . import comments, news
