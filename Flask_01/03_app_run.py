from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    # app.run()
    # app.run()的参数
    app.run(host="0.0.0.0", port=5000, debug = True)
    # host IP
    # port 端口
    # debug = True 开启debug的模式
    # debug 的作用----->django
    # - 修改代码之后
    # 开发服务器可以自动重启
    # - 后端代码出现错误之后，在前端页面会展示详细的错误信息
    # - 提供静态文件
    # flask的作用：
    # 开发服务器可以自动重启
    # - 后端代码出现错误之后，在前端页面会展示详细的错误信息