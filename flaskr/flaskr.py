#coding=utf-8

from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return '欢迎光临！'


@app.route('/login')
def login():
    return 'login page'


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/user/<username>')
def profile(username):
    return 'User %s' % username


@app.route('/about')
def about():
    return 'About page'

with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('profile', username='John Doe')


if __name__ == '__main__':
    app.debug = True
    app.run()