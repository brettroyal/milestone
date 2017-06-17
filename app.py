from flask import Flask
import localprac
app_lulu = Flask(__name__)
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

@app_lulu.route('/hello_page_lulu')
def hello_world_lulu():
    # this is a comment, just like in Python
    # note that the function name and the route argument
    # do not need to be the same.
    ticker='TGT'
    localprac.create_stock_json(ticker)
    localprac.create_bokeh_script(ticker)
    return localprac.generate_html(ticker)

if __name__ == '__main__':
    app_lulu.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)