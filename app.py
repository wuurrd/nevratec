import sys
import os

this_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_dir)

from nevratec.app import app
import nevratec.views
application = app.wsgi_app

if __name__ == '__main__':
    app.run(debug=True)
