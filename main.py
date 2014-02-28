""" main.py is the top level script.

Return "Hello World" at the root URL.
"""

import os
import webapp2

import sys
# sys.path includes 'server/lib' due to appengine_config.py
from flask import Flask
from flask import render_template
app = Flask(__name__.split('.')[0])
                                       
@app.route('/')
@app.route('/')
def mainpage(name=None):
  """ Return me template at application /me URL."""
  return render_template('me.html', name=name)

@app.route('/catwalk')
def catwalk(name=None):
  """ Return me template at application /me URL."""
  return render_template('catwalk.html', name=name)
  
@app.route('/madlibs')
def madlibs(name=None):
  """ Return me template at application /me URL."""
  return render_template('madlibs.html', name=name)





