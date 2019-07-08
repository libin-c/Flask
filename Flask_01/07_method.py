from flask import Flask

app = Flask(__name__)

# Flask 视图支持的访问方式是 默认是 GET  HEAD OPTIONS、
# OPTIONS 解决跨域问题的 是浏览器访问服务器的白名单和请求方式


# Django如何解决跨域问题
# 在中间件中 前期加入OPTIONS的请求验证的代码

# 中间件
# 客户端--->中间件前期处理--->视图---->中间件后期处理---->客户端

@app.route('/',methods=['POST'])
def View_one():
    return 'View_one'

@app.route('/view/2',methods=['GET','POST'])
def View_two():
    return 'View_two'

@app.route('/view/3')
def View_three():
    return 'View_three'


if __name__ == '__main__':
    app.run()
