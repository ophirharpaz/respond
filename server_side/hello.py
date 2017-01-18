from flask import Flask
app = Flask(__name__)
	
	
@app.route('/')
def intro():
	return 'Hello world!'
	
	
@app.route('/user/<username>')
def show_user_profile(username):
    return 'Hello, %s!' % (username, )