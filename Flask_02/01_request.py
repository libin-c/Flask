from werkzeug.routing import BaseConverter
from flask import Flask

app = Flask(__name__)


#
# request接收参数分为两种
# 01  路径拼接
#     1) 参数类型：参数名               eg:int:user_id  default int any path float uuid
#     2）参数类型（参数限制）：参数名称    eg:int(min=1):user_id
#     3）自定义  分3步  1 自定义类 regex 正则匹配  2 注册参数   3 装饰器中使用 记住BaseConverter
# 02  非路径拼接

# 1) 参数类型：参数名
# @app.route('/request/<joint>')
# def request_url_joint(joint):
#     return 'request url {}'.format(joint)

# 2）参数类型（参数限制）：参数名称
# @app.route('/request/<int(min=5):joint>')
# def request_url_joint(joint):
#     return 'request url {}'.format(joint)

class MobileConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'


app.url_map.converters['mobile'] = MobileConverter


@app.route('/request/<mobile:mobile>')
def request_url_mobile(mobile):
    return 'request url {}'.format(mobile)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
