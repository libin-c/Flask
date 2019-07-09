from flask import Flask
from users import user_bp

app = Flask(__name__)

app.redis_client = 'redis clent obj'

app.register_blueprint(user_bp)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
