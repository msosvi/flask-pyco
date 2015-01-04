# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.pyco import Site
from pygments_renderer import PygmentsRenderer

app = Flask(__name__)
app.debug = True
mistune_renderer = PygmentsRenderer()
site = Site(app,mistune_renderer=mistune_renderer)

if __name__ == '__main__':
    app.run()
