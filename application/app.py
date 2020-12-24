from flask import Flask, request, render_template, redirect
import psycopg2
from .validate_form import validate_email, validate_password
from .db import create_user, exists, conn

app=Flask(__name__)

@app.route('/')
def index():
    print(dir(request))
    return render_template('authorize.html')
    
    
@app.route('/new_user', methods=['POST'])
def new_user():
    
    uname = request.form.get('uname') 
    password = request.form.get('pass')
    val_uname, val_passwd = validate_email(uname), validate_password(password)
    
    if (not val_uname):
        return render_template('authorize.html', message='Invalid email address')
    elif (not val_passwd == 'valid'):
        return render_template('authorize.html', message=val_passwd)
    else: 
        status = create_user(uname, password)
        if (status == 'created'):
            return 'Dashboard'
        else: 
            return render_template('authorize.html', message=status)

    
@app.route('/login', methods=['POST'])
def user_auth():
    
    status = exists(uname, password)
    if (status):
        return 'Dashboard'
    else:
        return render_template('authorize.html', message='Wrong username or password')


