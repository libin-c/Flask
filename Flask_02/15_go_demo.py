from flask import Flask, g, abort

app = Flask(__name__)


@app.before_request
def authentication():
    """
    用户权限验证
    :return:
    """
    # g.user_id = 14
    g.user_id = None


def login_required(func):
    def wrapper(*args, **kwargs):
        if g.user_id is not None:

            return func(*args, **kwargs)
        else:
            abort(401)

    return wrapper


@app.route('/')
def no_decorator():
    return "g.user_id = {}".format(g.user_id)


@app.route('/decorator')
@login_required
def has_decorator():
    return "g.user_id ={} ".format(g.user_id)


if __name__ == '__main__':
    app.run()
