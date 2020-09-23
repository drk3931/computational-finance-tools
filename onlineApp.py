import configure
from flask import Flask,render_template
from flask import request,Response
from flask import jsonify
import json
import Stocks
import os

port = int(os.environ.get("PORT", 5000))

class InvalidUsage(Exception):
  def __init__(self, message, status_code=400, payload=None):
      Exception.__init__(self)
      self.status_code = status_code
      self.message = message
      self.payload = payload


app = Flask(__name__)
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'POST')
  return response


@app.errorhandler(InvalidUsage)
def handleError(invUsage):
    response = jsonify({'error':invUsage.message})
    response.status_code = invUsage.status_code
    return response

@app.route('/stockData', methods=["POST"])
def stockData():
  reqBody = request.json

  if reqBody is None:
    raise InvalidUsage('Please include 2 symbols.')

  if 'symbol1' in reqBody and 'symbol2' in reqBody:
    validSymbol1 = Stocks.validSymbol(reqBody['symbol1'])
    validSymbol2 = Stocks.validSymbol(reqBody['symbol2'])
    if validSymbol1 and validSymbol2:
      chart = Stocks.getPrice(reqBody['symbol1'],reqBody['symbol2'])
      return chart,200
    else:
      raise InvalidUsage('Please enter a valid symbol.',status_code=400)
  else:
    raise InvalidUsage('Please include 2 symbols.')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=port)