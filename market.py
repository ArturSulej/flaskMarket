from flask import Flask

app = Flask(__name__)  # Initialize Flask, get local python file name


@app.route('/')  # Decorator, website navigation
def hello_world():  # put application's code here
    return '<h1>Hello World</h1>'

@app.route('/about/<username>')     # Receive any string after about
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'


if __name__ == '__main__':
    app.run()
