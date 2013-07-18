import os

from flask import Flask


class Nevratec(Flask):
    def __init__(self, *args, **kwargs):
        Flask.__init__(self,
                       __name__,
                       static_folder='static',
                       template_folder="templates",
                       *args, **kwargs)
        self.config['DEBUG'] = os.environ.get('FLASK_DEBUG') is None

app = Nevratec()
