#!/bin/python3.8
from flask import Flask, render_template, request
from nsetools import Nse
app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form action="/create" methods="post">
            <input type="text" name="cmpname">
            <input type="submit">
        </form>
    '''
@app.route('/create', methods = ['GET'])
def create():
    cmp = request.args.get('cmpname')
    nse = Nse()
    quote = nse.get_quote(cmp)
    name = (quote['companyName'])
    bp = str(quote['buyPrice1'])
    ap = str(quote['averagePrice'])
    dh = str(quote['dayHigh'])
    dl = str(quote['dayLow'])
    #return 'Name: %s ' % dh
    dict = {'Name':name, 'Buy Price':bp, 'Avg Price':ap, 'Day High':dh, 'Day Low':dl}
    return render_template('stock.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)
