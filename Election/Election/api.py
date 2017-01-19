"""
 Api for data collection
"""

from Election import app
from flask import request
@app.route('/api')
@app.route('/api/')
def api():
	""" The start of the api"""
	return "The API call"

@app.route('/api/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		return 'login data sent to server'
	else:
		return 'get the login page'
    