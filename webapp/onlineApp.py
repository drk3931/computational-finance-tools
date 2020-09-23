import configure
from flask import Flask,render_template
from flask import request,Response
from flask import jsonify
import json
import Stocks


class InvalidUsage(Exception):
  def __init__(self, message, status_code=400, payload=None):
      Exception.__init__(self)
      self.status_code = status_code
      self.message = message
      self.payload = payload


app = Flask(__name__)
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', 'https://drk3931.github.io')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'POST')
  return response


@app.errorhandler(InvalidUsage)
def handleError(invUsage):