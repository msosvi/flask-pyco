# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.pyco import Site

app = Flask(__name__)
app.debug = True
site = Site(app)


if __name__ == '__main__':
    site.development = True
    app.run()
