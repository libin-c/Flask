import json

from flask import Flask, redirect, jsonify

app = Flask(__name__)


#

def func():
    a = 10
    b = 20
    c = 30
    # 这里相当于return (a, b, c)
    return a, b, c


#  这里页默认操作了(a,b,c) = func()
#  因为元祖可以赋值 所以 a = a , b = b ,c= c
a, b, c = func()


# return 后面的三个参数 ：
# 响应体  状态码  响应头
@app.route('/status')
def index():
    # return 'OK', 200, {'User': 'LiBin', 'Age': 18}
    return  'OK', 200,[('User'),('LiBin'),('Age'),(18)]

# 响应体  状态码
@app.route('/status')
def index():
    return 'OK', 200


# 响应体
@app.route('/')
def index():
    return 'OK'


if __name__ == '__main__':
    app.run()
