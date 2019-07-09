from flask import Flask, abort,request

app = Flask(__name__)


# errorhandler 自己定义错误 装饰器的方式


@app.errorhandler(404)
def handler_404_error(e):
    return  '坏的请求'
@app.errorhandler(ZeroDivisionError)
def handler_zero(e):
    return '除数不能为0'


@app.route('/')
def index():
    c = 1/0
    return 'index  {}'.format(c)


if __name__ == '__main__':
    app.run()