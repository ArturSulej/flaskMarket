from flask import Flask

app = Flask(__name__)  # Initialize Flask, get local python file name


@app.route('/')  # Decorator, website navigation
def hello_world():  # put application's code here
    return '<h1>Hello World bigger</h1>'


if __name__ == '__main__':
    app.run()
