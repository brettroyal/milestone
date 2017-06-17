import localprac
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

import requests
import simplejson as json
from pandas import *
import numpy as np
import bokeh
from bokeh.plotting import figure, show, output_file
from bokeh.resources import CDN
from bokeh.embed import file_html,components
from datetime import date,datetime

thevars={}

@app.route('/show_stocks',methods=['GET','POST'])
def show_stocks():
		arbnum=96
		if request.method == 'GET':
				return render_template('index.html',num=19) #looks for file in the template folde, returns html.
		else:
				ticker=request.form['ticker']
				return localprac.generate_html(ticker)
		return(ticker)

@app.route('/',methods=['GET'])
def index():
		arbnum=96
		if request.method == 'GET':
				return render_template('index.html',num=arbnum) #looks for file in the template folde, returns html.
		else:
				return 'request.method was not a GET!'
		

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='whispering-fortress-85064.herokuapp.com', port=5000)
    #app.run(host='127.0.0.1', port=5000)
    
