from werkzeug.routing import BaseConverter
from flask import Flask, request

app = Flask(__name__)


#
# request接收参数分为两种
# 01  路径拼接
#     1) 参数类型：参数名               eg:int:user_id  default int any path float uuid
#     2）参数类型（参数限制）：参数名称    eg:int(min=1):user_id
#     3）自定义  分3步  1 自定义类 regex 正则匹配  2 注册参数   3 装饰器中使用 记住BaseConverter
# 02  非路径拼接
#       1） 查询参数 args
#       2） 请求头  headers
#       3） 请求体
#         1   表单    form
#         2   非表单   data
#         3   文件    files

# 查询参数
@app.route('/page')
def paginater():
    pk = request.args.get('pk')
    return 'This is {} page'.format(pk)


@app.route('/upload', methods=['POST'])
def upload():
    image_file = request.files.get('pic')
    image_file.save('./2.png')
    # with open('./1.png', 'wb')as img_file:
    #     img_file.write(image_file.read())
    return 'save ok'


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
