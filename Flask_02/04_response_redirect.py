from flask import Flask,redirect

app = Flask(__name__)


# falsk response 完成的三种模式
# 1   渲染模板
# 2   重定向
# 3   返回json

# 重定向 和 Django 一样
@app.route('/')
def index():

    return redirect('https://www.baidu.com')





if __name__ == '__main__':
    app.run()
