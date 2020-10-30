import flask
from flask import Flask
import requests
from datetime import *; from dateutil.relativedelta import *
import pytz
import calendar

application = Flask(__name__)

#la = pytz.timezone("America/Los_Angeles")
#fmt = '%Y-%m-%d'
#now = datetime.now(la)
#print(now)
TODAY = date.today()
@application.route('/search/<stock1>')
def onSearch(stock1):
    headers = {
        'Content-Type': 'application/json'
    }
    requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/" + stock1 + "?token=4384f3e3de1ccddb51805eaf956b71edb0e7b25c",
        headers=headers)
    if (requestResponse != None):
        return flask.jsonify(requestResponse.json())


@application.route('/find/<stock2>')
def onFind(stock2):
    headers = {
        'Content-Type': 'application/json'
    }
    requestResponse = requests.get("https://api.tiingo.com/iex/" + stock2 + "?token=4384f3e3de1ccddb51805eaf956b71edb0e7b25c",
                                   headers=headers)
    if requestResponse != None:
        return flask.jsonify(requestResponse.json())

@application.route('/news/<stock3>')
def onNews(stock3):
    headers = {
        'Content-Type': 'application/json'
   }
    requestResponse = requests.get("https://newsapi.org/v2/everything?apiKey=8a56f5ee55814b13940b20f023103676&q=" + stock3, headers=headers)
    if requestResponse != None:
        return flask.jsonify(requestResponse.json())

date = TODAY+relativedelta(months=-6)
dateinp = str(date)
@application.route('/charts/<stock4>')
def onCharts(stock4):
    headers = {
       'Content-Type': 'application/json'
   }
    requestResponse = requests.get("https://api.tiingo.com/iex/" + stock4 + "/prices?startDate=" + dateinp +"&resampleFreq=12hour&columns=open,high,low,close,volume&token=4384f3e3de1ccddb51805eaf956b71edb0e7b25c", headers=headers)
    if requestResponse != None:
     #   print(requestResponse.json())
        return flask.jsonify(requestResponse.json())


@application.route('/')
def index():
    return (application.send_static_file('index.html'))


application.run(debug=True)
