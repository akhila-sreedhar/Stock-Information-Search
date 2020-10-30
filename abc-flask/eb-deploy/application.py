import flask
from flask import Flask
import requests
from datetime import *
from dateutil.relativedelta import *
import pytz

application = Flask(__name__,static_folder="static")

la = pytz.timezone("America/Los_Angeles")
now = datetime.now(la).date()

@application.route('/search/<stock1>')
def onSearch(stock1):
    headers = {
        'Content-Type': 'application/json'
    }
    requestResponse = requests.get(
        "https://api.tiingo.com/tiingo/daily/" + stock1 + "?token=4384f3e3de1ccddb51805eaf956b71edb0e7b25c",
        headers=headers)
    if requestResponse is not None:
        return flask.jsonify(requestResponse.json())


@application.route('/find/<stock2>')
def onFind(stock2):
    headers = {
        'Content-Type': 'application/json'
    }
    requestResponse = requests.get(
        "https://api.tiingo.com/iex/" + stock2 + "?token=4384f3e3de1ccddb51805eaf956b71edb0e7b25c",
        headers=headers)
    if requestResponse is not None:
        return flask.jsonify(requestResponse.json())


@application.route('/news/<stock3>')
def onNews(stock3):
    headers = {
        'Content-Type': 'application/json'
    }
    requestResponse = requests.get(
        "https://newsapi.org/v2/everything?apiKey=8a56f5ee55814b13940b20f023103676&q=" + stock3, headers=headers)
    if requestResponse is not None:
        return flask.jsonify(requestResponse.json())


date = now + relativedelta(months=-6)
dateinp = str(date)


@application.route('/charts/<stock4>')
def onCharts(stock4):
    headers = {
        'Content-Type': 'application/json'
    }
    requestResponse = requests.get(
        "https://api.tiingo.com/iex/" + stock4 + "/prices?startDate=" + dateinp + "&resampleFreq=12hour&columns=open,high,low,close,volume&token=4384f3e3de1ccddb51805eaf956b71edb0e7b25c",
        headers=headers)
    if requestResponse is not None:
        return flask.jsonify(requestResponse.json())


@application.route('/')
def index():
    return application.send_static_file('index.html')

if __name__ == "__main__":
    application.run(debug=True)
