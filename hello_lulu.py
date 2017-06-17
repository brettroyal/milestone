from flask import Flask
import localprac
app_lulu = Flask(__name__)

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