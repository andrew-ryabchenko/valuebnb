from flask import Flask, request, render_template, redirect, make_response
from validate_form import validate_email, validate_password
from db import create_user, exists, conn

app=Flask(__name__)

#Main route of the application. If authorized client with cookies set, redirects to dashboard. 
@app.route('/')
def index():
    if (request.cookies.get('user_email')):
        return redirect('/dashboard', 303)
    else:
        return render_template('authorize.html')
    
# Verifies user in database
@app.route('/login', methods=['POST'])
def login():

    user_email=request.headers['user_email']
    password = request.headers['password']
    # Database verification
    # If user is found in the database respond with <`user_status`: `found`> header
    if(user_email and password):
        if(exists(user_email, password)):
            response = make_response()
            response.headers['user_email'] = user_email
            response.headers['user_status'] = 'found'
            return response
    # If user is not found in the database respond with <`user_status`: `not_found`> header
        else:
            response = make_response()
            response.headers['user_email'] = user_email
            response.headers['user_status'] = 'not_found'
            return response
    else:
        return redirect('/', 303)

# Attempts to register new user
@app.route('/register', methods=['POST'])
def register():
    user_email=request.headers['user_email']
    password = request.headers['password']

    if(user_email and password):
        status = create_user(user_email, password)
        # If status==100 and user is registered return 
        # Sets headers <`user_status`: `registered`>, <`user_email`: {user_email}>
        if (status==100):
            response = make_response()
            response.headers['user_email'] = user_email
            response.headers['user_status'] = 'registered'
            return response
        # If status==101 and user is registered return 
        # Sets headers <`user_status`: `registered`>, <`user_email`: {user_email}>
        else:
            response = make_response()
            response.headers['user_email'] = user_email
            response.headers['user_status'] = 'already_exists'
            return response
    else:
        return redirect('/', 303)


# Return dashboard of the authorized user. If user is not authorized then redirects to the main page
@app.route('/dashboard')
def dashboard():
    user_email = request.cookies.get('user_email');
    if (user_email):
        # TODO pull user activity history from db
        return render_template('dashboard.html', data=user_email)
    else:
        return redirect('/', 303)



if __name__=='__main__':
    app.run(debug=True)   


