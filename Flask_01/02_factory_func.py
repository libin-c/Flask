from flask import Flask
import  os

app = Flask(__name__)


class DefaultConfig(object):
    MYSQL_CONFIG = 'Flask mysql 1'
    REDIS_CONFIG = 'Flask redis 1'

class TestConfig(DefaultConfig):
    MYSQL_CONFIG = 'Flask mysql 4'

def create_app(config):
    app.config.from_object(config)
    app.config.from_envvar('DEMO')
    return app


@app.route('/')
def helloWord():
    print(app.config.get('MYSQL_CONFIG'))
    return "hello  world"


if __name__ == '__main__':
    app.run()
