from flask import Flask, g

app = Flask(__name__)


@app.route('/')
def index():
    g.username = 'libin'
    g.sex = 1
    go_obj()
    return 'ok'


def go_obj():
    username = g.username
    sex = g.sex
    print('username = {} , sex = {}'.format(username, sex))


if __name__ == '__main__':
    app.run()