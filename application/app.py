from flask import Flask, request, render_template, redirect, make_response
from validate_form import validate_email, validate_password
from db import create_user, exists, conn

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('authorize.html')
    
@app.route('/login', methods=['POST'])
def login():
    user_email=request.headers['user_email']
    password = request.headers['password']
    # TODO database verification

    if (True):
        response = make_response(render_template('dashboard.html', data=user_email))
        response.headers['user_email'] = user_email
        return response

if __name__=='__main__':
    app.run(debug=True)   


