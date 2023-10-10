from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Home'


@app.route('/hello')
def helloIndex():
    return 'hello from flask'


app.run(host='0.0.0.0', port=5000)

# from website import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)
