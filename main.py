from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
    return f"<p>Hello, {name}!</p>"

@app.route('/home')
@app.route('/')
def main():
    return render_template('home.html', homeText = "Hello, World")