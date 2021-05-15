from assessment2.v import v
from flask import redirect, make_response

# example
@v.route('/logout', methods=['GET'])
def logout():
    response = make_response(redirect('/login'))
    response.delete_cookie('email')
    return response
