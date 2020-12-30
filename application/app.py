from flask import Flask, request, render_template, redirect, make_response
from validate_form import validate_email, validate_password
from db import create_user, exists
from helper_functions import *

app=Flask(__name__)

#Main route of the application. If authorized client with cookies set, redirects to dashboard. 
@app.route('/')
def index():
    if (request.cookies.get('email')):
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
    # and email_hash
    if(user_email and password):
        email_hash = exists(user_email, password)
        if (email_hash!=101):
            if(email_hash):
                response = make_response()
                response.headers['email_hash'] = email_hash
                response.headers['user_status'] = 'found'
                return response
        # If user is not found in the database respond with <`user_status`: `not_found`> header
            else:
                response = make_response()
                response.headers['user_status'] = 'not_found'
                return response
        else: #exists() returns database error 101, returns <`user_status`: `Try again later`>
            response = make_response()
            response.headers['user_status'] = 'Try again later'
            return response

    else: #Redirect to login page if credentials were missing
        return redirect('/', 303)

# Attempts to register new user
@app.route('/register', methods=['POST'])
def register():
    user_email=request.headers['user_email']
    password = request.headers['password']

    if(user_email and password):
        email_hash = create_user(user_email, password)
        # email_hash==101: database error somewhere along the way
        # email_hash==False: user already exists
        # email_hash==String: user successfully registered and email_hash is returned
        if (email_hash!=101): 
            if (email_hash):
                response = make_response()
                #response.headers['user_email'] = user_email
                response.headers['user_status'] = 'registered'
                response.headers['email_hash'] = email_hash
                return response
            else:
                response = make_response()
                response.headers['user_status'] = 'already_exists'
                return response

        else:
            response = make_response()
            response.headers['user_status'] = 'Try again later'
            return response
    else: #Redirect to login page if credentials were missing
        return redirect('/', 303)


# Return dashboard of the authorized user. If user is not authorized then redirects to the main page
@app.route('/dashboard')
def dashboard():
    user_email = request.cookies.get('email')
    email_hash = request.cookies.get('email_hash')
    
    if (user_email and email_hash):
        # TODO pull user activity history from db
        return render_template('dashboard.html', data=user_email, bathroom_types=bathrooms_la(), 
                                property_types=property_types_la())
    else:
        return redirect('/', 303)

@app.route('/estimate/<params>')
def estimate(params):
    print(parse_url(params))
    return 'something'


if __name__=='__main__':
    app.run(debug=True)   


