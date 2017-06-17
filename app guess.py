from flask import Flask, render_template, request, redirect
import requests
import simplejson as json
from flask import Flask, render_template, request, redirect
import requests
import simplejson as json
from pandas import *
import numpy as np
import matplotlib.pyplot as plt
import bokeh
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.iris import flowers
from datetime import date,datetime
import sys
#quandl api key : xtA72oRe4ZL-CZRfuMuU


app = Flask(__name__)

@app.route('/')


def main():
	ticker=getticker()
	create_stock_json(ticker)
	create_bokeh_script(ticker)
	#REad JSON and set up dataframe
	return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)
