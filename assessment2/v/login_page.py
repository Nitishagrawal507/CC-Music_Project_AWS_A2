from assessment2.v import v
from assessment2.models import aws_login
from flask import make_response, redirect, request, render_template


@v.route('/login', methods=['GET'])
def login_page():
    return render_template('login_page.html')


@v.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    psw = request.form['password']

    all_set = aws_login.authenticate_user(email, psw)

    if all_set:
        response = make_response(redirect('/'))
        response.set_cookie('email', email)
        return response
    else:
        return render_template('login_page.html', loginError='Email or password is invalid')
