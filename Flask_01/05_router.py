from flask import  Flask

app = Flask(__name__)


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