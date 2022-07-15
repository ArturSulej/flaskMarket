from market import app
from flask import render_template
from market.models import Item

@app.route('/')  # Decorator, website navigation
@app.route('/home')
def home_page():  # put application's code here
    return render_template('home.html')    # Importing template from templates folder

@app.route('/market')
def market_page():
    items = Item.query.all()    # Get all elements from table Item
    return render_template('market.html', items=items) #Send data to html
