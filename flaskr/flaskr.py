import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from contextlib import closing

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application:)
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
# app.config.from_object(DATABASE)


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request():
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()


def connect_db():
    # print '%s' % app.config
    return sqlite3.connect(app.config.from_object(DATABASE))  #sqlite3.connect(app.config['DATABASE'])


if __name__ == '__main__':
    app.run(host='0.0.0.0')