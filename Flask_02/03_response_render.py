from flask import Flask, render_template

app = Flask(__name__)


# falsk response 完成的三种模式
# 1   渲染模板
# 2   重定向
# 3   返回json

#
# @app.route('/')
# def index():
#
#     return render_template('index.html',mysrc='http://www.baidu.com',mystr='百度')

# 这里应用了一个**args 解包



@app.route('/')
def index():
    data = {
        'mysrc': 'http://www.baidu.com',
        'mystr': '百度'
    }
    return render_template('index.html', **data)


if __name__ == '__main__':
    app.run()
