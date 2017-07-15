import json
import requests
from bs4 import BeautifulSoup
import urllib
import lxml
from os import system
from flask import Flask, request, jsonify

# ES and VIX futures data scraper

cboe = 'http://www.cboe.com/products/vix-index-volatility/vix-options-and-futures/vix-index'
cme = 'http://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500.html'


def scrape_vix(link):
    results = requests.get(link)
    c = results.content
    soup = BeautifulSoup(c, "lxml")
    table = soup.find('table')
    data = []
    table_data = table.findAll('td')
    for items in table_data:
        text = items.find(text=True)
        data.append(text)
    x = data[7]
    return x

def scrape_es(link):
    results = requests.get(link)
    c = results.content
    soup = BeautifulSoup(c, "lxml")
    table = soup.find('table')
    data = []
    table_data = table.findAll('td')
    for items in table_data:
        text = items.find(text=True)
        data.append(text)
    y = data[3]
    return y

app = Flask(__name__)

@app.route('/<string:name>', methods = ['GET'])

def get_futures(name):
    futures = [
    {
        'id': 'vix_futures',
        'value': scrape_vix(cboe)
    },
    {
        'id': 'es_futures',
        'value': scrape_es(cme)
    }
    ]
    
    if name == 'vix':
        return jsonify(futures[0])
    else:
        return jsonify(futures[1])

if __name__ == '__main__':
    app.run(debug=True)

