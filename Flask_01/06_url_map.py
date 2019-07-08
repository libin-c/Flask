import json

from flask import  Flask

app = Flask(__name__)

# @app.route('/')
# def route_map():
#     """
#     主视图，返回所有视图网址
#     """
#     rules_iterator = app.url_map.iter_rules()
#     return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})

@app.route('/')
def route_map():
    """
    编写路由函数
    url_map  Map对象 保存了全部的路由信息
    app.url_map.iter_rules() 获得map对象中的路由列表
    :return:
    """
    return json.dumps({'api':{item.rule:item.endpoint for item in app.url_map.iter_rules()}})


@app.route('/view/1')
def View_one():
    return 'View_one'

@app.route('/view/2')
def View_two():
    return 'View_two'

@app.route('/view/3')
def View_three():
    return 'View_three'

if __name__ == '__main__':
    app.run()
