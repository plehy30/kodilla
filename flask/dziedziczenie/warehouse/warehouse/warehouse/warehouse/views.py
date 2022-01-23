"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from warehouse import app

@app.route('/child')
def warehouse():
    items = ['screwdriver', 'hammer', 'saw']
    errors = ['hammer is broken']
    return render_template('child.html', items=items, errors=errors)