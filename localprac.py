from flask import Flask, render_template, request, redirect
import requests
import simplejson as json
from pandas import *
import numpy as np
import bokeh
from bokeh.plotting import figure, show, output_file
from bokeh.resources import CDN
from bokeh.embed import file_html,components
from datetime import date,datetime
import sys

def get_ticker():
	#quandl api key : xtA72oRe4ZL-CZRfuMuU
	#Get Ticker and pull dat and write it into the JSON
	#ticker = raw_input("Please enter ticker!!! ")
	ticker="MSFT"
	#curl "https://www.quandl.com/api/v3/datasets/WIKI/FB/data.json?api_key=YOURAPIKEY"
	return ticker

def create_stock_json(ticker):
	request='https://www.quandl.com/api/v3/datasets/WIKI/'+ticker+'/data.json?api_key=xtA72oRe4ZL-CZRfuMuU'
	r=requests.get(request)
	print r.text[1:14]
	if r.text[1:14]!='"dataset_data':
		print "yeah ydude error"
		return False
	f=open('miguel.json','w')
	f.write(r.text)
	f.close()
	print "We got to line 31"
	return True
def create_bokeh_script(ticker):
	df=read_json('https://www.quandl.com/api/v3/datasets/WIKI/'+ticker+'/data.json?api_key=xtA72oRe4ZL-CZRfuMuU')
	print "got to line 35"
	data=df.dataset_data['data']
	cols=df.dataset_data['column_names']
	stox=DataFrame(data=data,columns=cols)
	stox['Date']=to_datetime(stox['Date'],infer_datetime_format=True,format='%Y%m%d%f') #change eveyrthing from regualr object to datetime
	p = figure(width=800, height=250, x_axis_type="datetime", title=ticker + " Price Over Time")
	p.line(stox['Date'], stox['Close'], color='navy', alpha=0.5)
	#output_file("template/graph.html")

#	show(p)
	script,div=components(p)
	# s=open('templates/script.html','w')
	# s.write(script)
	# s.close()
	# d=open('templates/div.html','w')
	# d.write(div)
	# d.close()


	return script,div

def generate_html(ticker):
	script,div=create_bokeh_script(ticker)
	div+="b"
	html='''<!doctype html>
	<html lang="en">
		<head>
		<title="Let's get financial.">
		<link rel=stylesheet type=text/css href='static/style.css'>
			<meta charset="utf-8">
			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
			<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
			'''+script+'''
			<link href="https://cdn.pydata.org/bokeh/release/bokeh-0.12.6.min.css" rel="stylesheet" type="text/css">
			<link href="https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.6.min.css" rel="stylesheet" type="text/css">
			<script src="https://cdn.pydata.org/bokeh/release/bokeh-0.12.6.min.js"></script>
			<script src="https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.6.min.js"></script>
		</head>
		<body>
		<div class=page>
  <h1>Gimmme.</h1>
  <div class=metanav>

    <h4>
      We want a stock ticker.
    </h4>

    <form id='symbol' method='POST' action='show_stocks' >
      <p>
    Symbol: <input type='text' name='ticker' />
      </p>
      <p>
    <input type='submit' value='Select' />
      </p>
    </form>

  </div>
</div>
			<div align='right'>
			</div>'''+div+'''
		</body>
	</html>'''

	return html

#ticker=get_ticker()

#ticker='MSFT'
#generate_html(ticker)
#create_stock_json(ticker)

