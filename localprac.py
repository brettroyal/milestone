from flask import Flask, render_template, request, redirect
import requests
import simplejson as json
from pandas import *
import numpy as np
import bokeh
from bokeh.plotting import figure, show, output_file
from bokeh.resources import CDN
from bokeh.palettes import Category10
from bokeh.embed import file_html,components
from datetime import date,datetime
import sys
import re

def get_ticker():
	#quandl api key : xtA72oRe4ZL-CZRfuMuU
	#Get Ticker and pull dat and write it into the JSON
	#ticker = raw_input("Please enter ticker!!! ")
	ticker="MSFT"
	#curl "https://www.quandl.com/api/v3/datasets/WIKI/FB/data.json?api_key=YOURAPIKEY"
	return ticker

def good_ticker(ticker):
	request='https://www.quandl.com/api/v3/datasets/WIKI/'+ticker+'/data.json?api_key=xtA72oRe4ZL-CZRfuMuU'
	r=requests.get(request)
	if r.text[1:14]!='"dataset_data':
		return False
	return True

def create_bokeh_script(ticker):
	print ticker + " is the ticker we got sent."
	ticker=ticker.replace(' ','')
	print ticker+ " is ticker"

	ticker_list=ticker.split(',')
	errors=""
	p = figure(width=800, height=250, x_axis_type="datetime", title=ticker + " Price Over Time")
	total_stocks=len(ticker_list)
	
	if total_stocks>2:
		color_list=Category10[total_stocks]
	else:
		color_list=['blue','red']
	t=0

	for oneticker in ticker_list:
		if good_ticker(oneticker):
			print oneticker
			df=read_json('https://www.quandl.com/api/v3/datasets/WIKI/'+oneticker+'/data.json?api_key=xtA72oRe4ZL-CZRfuMuU')
			data=df.dataset_data['data']
			cols=df.dataset_data['column_names']
			stox=DataFrame(data=data,columns=cols)
			stox['Date']=to_datetime(stox['Date'],infer_datetime_format=True,format='%Y%m%d%f') #change eveyrthing from regualr object to datetime
			#p = figure(width=800, height=250, x_axis_type="datetime", title=ticker + " Price Over Time")
			p.line(stox['Date'], stox['Close'], alpha=0.5,legend=oneticker, line_color=color_list[t])
		else:
			errors+=oneticker + ' was a bad ticker.  Call a cardiologist.<br />'
		t+=1
	#p.line(colors='Set1')
	script,div=components(p)
	return script,div,errors

def generate_html(ticker):
	script,div,errors=create_bokeh_script(ticker)
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
      Enter up to 10 stocks, with commas.
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
			<div>'''+errors+'''</div>
		</body>
	</html>'''

	return html

