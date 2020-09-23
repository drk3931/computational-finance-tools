import configure
import flask
from flask import Flask,render_template,make_response
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

def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response



@app.errorhandler(InvalidUsage)
def handleError(invUsage):
    response = jsonify({'error':invUsage.message})
    response.status_code = invUsage.status_code
    return response

@app.route('/stockData', methods=["POST"])
def stockData():
  reqBody = request.json

  if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()

  if reqBody is None:
    raise InvalidUsage('Please include 2 symbols.')

  if 'symbol1' in reqBody and 'symbol2' in reqBody:
    validSymbol1 = Stocks.validSymbol(reqBody['symbol1'])
    validSymbol2 = Stocks.validSymbol(reqBody['symbol2'])
    if validSymbol1 and validSymbol2:
      response = flask.jsonify({'chart': Stocks.getPrice(reqBody['symbol1'],reqBody['symbol2'])})
      response.headers.add('Access-Control-Allow-Origin', '*')
      return response,200
    else:
      raise InvalidUsage('Please enter a valid symbol.',status_code=400)
  else:
    raise InvalidUsage('Please include 2 symbols.')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
