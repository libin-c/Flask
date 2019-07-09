from flask import Flask, make_response

app = Flask(__name__)



# 响应体  状态码  响应头
@app.route('/status')
def old_index():
    # return 'OK', 200, {'User': 'LiBin', 'Age': 18}
    return  'OK', 200,[('User'),('LiBin'),('Age'),(18)]



# 响应体
@app.route('/')
def index():
    resp = make_response('OK')
    resp.status = '404'
    resp.headers =  {'User': 'LiBin', 'Age': 18}
    return  resp


if __name__ == '__main__':
    app.run()
