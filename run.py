from flask.templating import render_template
from assessment2 import assessment2

if __name__ == '__main__':
    assessment2.run(host='127.0.0.1', port=5000, debug=True)#for local
