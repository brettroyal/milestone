from flask import Flask, render_template, request, redirect
import requests
import simplejson as json

#quandl api key : xtA72oRe4ZL-CZRfuMuU


app = Flask(__name__)

@app.route('/')
def main():

	
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)
