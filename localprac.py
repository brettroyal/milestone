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
#Get Ticker and pull dat and write it into the JSON
ticker = raw_input("Please enter ticker!!! ")
#ticker="MSFT"
#curl "https://www.quandl.com/api/v3/datasets/WIKI/FB/data.json?api_key=YOURAPIKEY"
request='https://www.quandl.com/api/v3/datasets/WIKI/'+ticker+'/data.json?api_key=xtA72oRe4ZL-CZRfuMuU'
r=requests.get(request)
f=open('john.json','w')
f.write(r.text)
f.close()

#REad JSON and set up dataframe
df=read_json('john.json')

data=df.dataset_data['data']
cols=df.dataset_data['column_names']
stox=DataFrame(data=data,columns=cols)
stox['Date']=to_datetime(stox['Date'],infer_datetime_format=True,format='%Y%m%d%f') #change eveyrthing from regualr object to datetime


p = figure(width=800, height=250, x_axis_type="datetime", title=ticker + " Price Over Time")
p.line(stox['Date'], stox['Close'], color='navy', alpha=0.5)
output_file("graph.html")

show(p)