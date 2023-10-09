from flask import Flask


app = Flask(__name__)

""" main page """


@app.route('/')  # static route
def index():
    return 'Home'


""" Dynamic route """


@app.route('/hello/<string:name>/')
def post(name):
    return f'hello from {name}'


"""Dynamic route with two optional parameters"""


@app.route('/hello/<name>/<age>/')
def getpost(name, age):
    return f'hello from {name} who is {age}'


app.run(host='0.0.0.0', port=5000)
