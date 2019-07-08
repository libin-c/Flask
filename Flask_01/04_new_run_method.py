from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'

# - FLASK_ENV=development 开发模式
# - FLASK_ENV=production  生产模式  默认
