#coding:utf-8

from flask import Flask, url_for
from flask import request
from werkzeug import secure_filename, abort, redirect

app = Flask(__name__)

@app.route('/hello')
def hello_world():
	return 'Hello World!'

@app.route('/')
def index():
	return 'Index Page'

@app.route('/user/<username>/')
def show_user_profile(username):
	'show the user profile for that user'
	return 'User is %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	'show the post with the given id, the id is an integer'
	return 'Post %d' % post_id

@app.route('/projects/')
def projects():
	return 'The project page'

@app.route('/about')
def about():
	return abort(401)
	return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
#	error = None
    if request.method == 'POST':
    	if valid_login(request.form['username'], request.form['password']):
    		return log_the_user_in(request.form['username'])
    	else:
    		return "{\n result:0, \n detail:'user name is incorrect'\n}" 
        #return 'do the login'
    else:
        return 'show the login form'
    pass

def valid_login(username, password):
	if username == 'Jerry':
		return True
	else:
		return False

def log_the_user_in(username):
	return "{id:1, 'when':'moning', username:'%s'}" % username

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['the_file']
		if f.save('/users/Jerry/code/FlaskDemo/' + secure_filename(f.filename)):
			return 'upload successful'
		else:
			return 'upload fail.'

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')