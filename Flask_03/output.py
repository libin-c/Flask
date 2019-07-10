from flask import make_response, current_app
from flask_restful.utils import PY3
from json import dumps


def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""

    # 是flask-restful提供的原始处理视图输出结果的方法
    #     # 传入参数说明
    #     # data -> 视图返回的字典数据
    #     # code -> 视图返回的状态码数据
    #     # headers -> 视图返回的响应头数据
    #
    #     # 需求分析
    #     # 视图可能返回 data  {'user_id': , 'name': }
    #
    #     # 只对视图正确输出做处理，对于视图返回的错误信息，不做处理
    if 'message' not in data:
        data = {
            'message': 'ok',
            'data': data
        }

    settings = current_app.config.get('RESTFUL_JSON', {})

    # If we're in debug mode, and the indent is not set, we set it to a
    # reasonable value here.  Note that this won't override any existing value
    # that was set.  We also set the "sort_keys" value.
    if current_app.debug:
        settings.setdefault('indent', 4)
        settings.setdefault('sort_keys', not PY3)

    # always end the json dumps with a new line
    # see https://github.com/mitsuhiko/flask/pull/1262
    dumped = dumps(data, **settings) + "\n"

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp
