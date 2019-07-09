from flask import Flask, make_response, request

app = Flask(__name__)


# cookie 的应用
# delete 实质上是Set-Cookie: username=; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=0; Path=/

# 1   创建cookie

@app.route('/set_cookie')
def set_cookie():
    resp = make_response('set_cookie')
    resp.set_cookie('username', 'libin', max_age=3600)
    return resp


# 2   获取cookie
@app.route('/get_cookie')
def get_cookie():
    c = request.cookies.get('username')
    return 'cookie value is {}'.format(c)

# 3   删除cookie
@app.route('/delete')
def delete_cookie():
    resp = make_response('delete cookie')
    resp.delete_cookie('username')
    return resp

if __name__ == '__main__':
    app.run()