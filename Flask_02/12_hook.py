from flask import Flask, abort, request

app = Flask(__name__)


# hook 钩子函数分为4步
# 1   before_first_request
# 在处理第一个请求之前执行
# 2   before_request
# 在处理每个请求前执行
# 3   after_request
# 在处理每个请求后执行 （视图函数没有抛出错误）
# 4   teardown_request
# 在每个请求最后执行
@app.before_first_request
def before_first_request():
    print('before_first_request')


@app.before_request
def before_request():
    print('before_request')


@app.after_request
def after_request(response):
    response.headers['Content-Type']='application/json'
    print('after_request')
    return response


@app.teardown_request
def teardown_request(response):
    print('teardown_request')


@app.route('/')
def index():
    return 'view is uesd'


if __name__ == '__main__':
    app.run(debug=True)
