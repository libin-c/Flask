from flask import Flask
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser
from flask_restful import inputs
import re

app = Flask(__name__)

api = Api(app)

# reqparse 提供的方法
# 1 required 必传参数
# 2 help 检验错误的时候返回的错误的信息
# 3 action
# 描述对于请求参数中出现多个同名参数时的处理方式
# action 默认值是 store 选取多个同名参数的第一个 其余的删除
#    action = 'append' 选取多个同名参数 装在一个列表中
# 4 type
# 描述参数应该匹配的类型，可以使用python的标准数据类型string、int，也可使用Flask-RESTful提供的检验方法，还可以自己定义
"""
1    url

2    regex(指定正则表达式)

    from flask_restful import inputs
    rp.add_argument('a', type=inputs.regex(r'^\d{2}&'))
3   natural 自然数0、1、2、3...

4   positive 正整数 1、2、3...

5   int_range(low ,high) 整数范围

6   rp.add_argument('a', type=inputs.int_range(1, 10))
7   boolean
"""

# 5   自定义
#
# 6 location 描述参数应该在请求数据中出现的位置
# location='form' 'args' 'cookie','files'
# 多个位置
# location = ['args', 'files']


def mobile_checkout(phone):
    '''
    检查手机号
    :param phone:
    :return:
    '''
    if re.match(r'^1[3-9]\d{9}$', phone):
        return phone
    else:
        raise ValueError('{} is not a valid mobile'.format(phone))


class LoginResource(Resource):

    def get(self):
        res_parser = RequestParser()
        res_parser.add_argument('user_id', required=True, action='append', type=int)
        res_parser.add_argument('sex', required=True, help='missing a param')
        res_parser.add_argument('age', required=True, type=inputs.int_range(1, 100))
        res_parser.add_argument('phone', required=True, type=mobile_checkout)
        res = res_parser.parse_args()

        user_id = res.user_id
        sex = res.sex
        age = res.age
        phone = res.phone
        return {'data': {'user_id': user_id, 'sex': sex, 'age': age, 'phone': phone}}


api.add_resource(LoginResource, '/user')

if __name__ == '__main__':
    app.run()
