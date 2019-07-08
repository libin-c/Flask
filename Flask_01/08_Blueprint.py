from flask import Flask

from user import user_bp
from news import news_bp,comments_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(news_bp)
app.register_blueprint(comments_bp)

@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
