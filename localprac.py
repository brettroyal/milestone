from flask import Flask, render_template, request, redirect
import requests
import simplejson as json
from pandas import *
import numpy as np
import matplotlib.pyplot as plt
import bokeh
from bokeh.plotting import figure, show, output_file
from bokeh.resources import CDN
from bokeh.embed import file_html,components
from datetime import date,datetime
import sys

def get_ticker():
	#quandl api key : xtA72oRe4ZL-CZRfuMuU
	#Get Ticker and pull dat and write it into the JSON
	ticker = raw_input("Please enter ticker!!! ")
	#ticker="MSFT"
	#curl "https://www.quandl.com/api/v3/datasets/WIKI/FB/data.json?api_key=YOURAPIKEY"
	return ticker

def create_stock_json(ticker):
	request='https://www.quandl.com/api/v3/datasets/WIKI/'+ticker+'/data.json?api_key=xtA72oRe4ZL-CZRfuMuU'
	r=requests.get(request)
	f=open('john.json','w')
	f.write(r.text)
	f.close()
	return
def create_bokeh_script(ticker):
	df=read_json('john.json')
	data=df.dataset_data['data']
	cols=df.dataset_data['column_names']
	stox=DataFrame(data=data,columns=cols)
	stox['Date']=to_datetime(stox['Date'],infer_datetime_format=True,format='%Y%m%d%f') #change eveyrthing from regualr object to datetime


	p = figure(width=800, height=250, x_axis_type="datetime", title=ticker + " Price Over Time")
	p.line(stox['Date'], stox['Close'], color='navy', alpha=0.5)
	#output_file("template/graph.html")

	show(p)
	script,div=components(p)

	s=open('templates/script.html','w')
	s.write(script)
	s.close()
	d=open('templates/div.html','w')
	d.write(div)
	d.close()


	return script,div

def generate_html(ticker):
	script,div=create_bokeh_script(ticker)
	html='''<!doctype html>
	<html lang="en">
		<head>
			<meta charset="utf-8">
			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
			<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
			'''+script+'''
			<link href="http://cdn.pydata.org/bokeh/release/bokeh-0.12.6.min.css" rel="stylesheet" type="text/css">
			<link href="http://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.6.min.css" rel="stylesheet" type="text/css">
			<script src="http://cdn.pydata.org/bokeh/release/bokeh-0.12.6.min.js"></script>
			<script src="http://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.6.min.js"></script>
		</head>
		<body>
			<div>
			</div>'''+div+'''
		</body>
	</html>'''

	return html

#ticker=get_ticker()

#ticker='MSFT'
#generate_html(ticker)
#create_stock_json(ticker)

