"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

@app.route('/warehouse')
def warehouse():
    items = ['screwdriver', 'hammer', 'saw']
    errors = ['hammer is broken']
    return render_template('warehouse.html', items=items, errors=errors)
