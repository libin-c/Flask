from flask import Flask, abort,request

app = Flask(__name__)

# abort()  抛出异常
@app.route('/article')
def get_article():

    number = request.args.get('number')
    if number is None:
        abort(400)
    return '{}'.format(number)


if __name__ == '__main__':
    app.run()