from assessment2.v import v
from flask import render_template, request, redirect
from assessment2.models import aws_login


@v.route('/register', methods=['GET'])
def register_page():
    return render_template('registration.html')


@v.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    uname = request.form['username']
    psw = request.form['password']

    user_added = aws_login.put_user(email, uname, psw)

    if user_added:
        return redirect('/login')
    else:
        return render_template('registration.html', registerError='The email already exists')
