from flask import Flask, render_template

app = Flask(__name__)  # Initialize Flask, get local python file name


@app.route('/')  # Decorator, website navigation
@app.route('/home')
def home_page():  # put application's code here
    return render_template('home.html')    # Importing template from templates folder

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '146865432172', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '964375219750', 'price': 150}
    ]   # List of 3 dictionaries
    return render_template('market.html', items=items) #Send data to html

if __name__ == '__main__':
    app.run()
