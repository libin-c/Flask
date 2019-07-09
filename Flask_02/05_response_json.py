import json

from flask import Flask,redirect,jsonify

app = Flask(__name__)


# falsk response 完成的三种模式
# 1   渲染模板
# 2   重定向
# 3   返回json


# 这里介绍两种返回json的方式
# 1 json.dumps
# 2 jsonify



# 1 json.dumps  返回的请求头 Content-Type: text/html; charset=utf-8
@app.route('/')
def index():
    json_dict = {
        "user_id": 11,
        "name":'张三'

    }
    return json.dumps(json_dict)

# 1 jsonify 返回的请求头 Content-Type: application/json
@app.route('/json')
def response_jsonify():
    json_dict = {
        "user_id": 11,
        "name":'张三'

    }
    return jsonify(json_dict)



if __name__ == '__main__':
    app.run()
