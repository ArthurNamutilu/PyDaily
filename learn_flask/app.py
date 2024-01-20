#!/usr/bin/python3
from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set the base directory
base_dir = os.path.abspath(os.path.dirname(__file__))
DB_NAME = "data.db"
# configuring the flask application for SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# creating a SQLAlchemy instance
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# initialising the database
with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
    return render_template('index.html', message="Learning flask framework", word='flask')


@app.route('/user/<username>')
def show_user(username):
    return f'The user is {username}'


# route to interact with database
@app.route('/add_user/<username>/<email>')
def add_user(username, email):
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return f"User {username} added!"


if __name__ == '__main__':
    app.run(debug=True)
