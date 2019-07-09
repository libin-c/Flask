from flask import Flask, session

app = Flask(__name__)

# session 的应用  session 和dict 一样 flask 吧session 存到了cookie里所以才需要加密
class DefaultConfig(object):
    SECRET_KEY = 'wqkdsdadmasda'

app.config.from_object(DefaultConfig)

# 1 创建session


@app.route('/set_session')
def set_session():
    session['user_id']=18
    session['username']='libin'
    return 'Ok'

# 2 获取session
@app.route('/get_session')
def get_session():
    user_id = session.get('user_id')
    return 'use_id  is {}'.format(user_id)

if __name__ == '__main__':
    app.run()
