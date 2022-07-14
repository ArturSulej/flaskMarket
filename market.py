from flask import Flask, render_template

app = Flask(__name__)  # Initialize Flask, get local python file name


@app.route('/')  # Decorator, website navigation
@app.route('/home')
def home_page():  # put application's code here
    return render_template('home.html')    # Importing template from templates folder

if __name__ == '__main__':
    app.run()
