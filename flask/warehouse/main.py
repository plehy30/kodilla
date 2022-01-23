from flask import Flask

app = Flask(__name__)
from flask import render_template, request, redirect


@app.route('/warehouse')
def warehouse():
    items = ['screwdriver', 'hammer', 'saw']
    errors = ['hammer is broken']
    return render_template('warehouse.html', items=items, errors=errors)
