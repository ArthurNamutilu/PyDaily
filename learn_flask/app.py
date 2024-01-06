from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', message="Learning flask framework", word='flask')


@app.route('/user/<username>')
def show_user(username):
    return f'The user is {username}'


if __name__ == '__main__':
    app.run(debug=True)
