from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
    return f"<p>Hello, {name}!</p>"

@app.route('/home')
@app.route('/')
def main():
    app.logger.info("Loading home page... ")
    return render_template('index.html', homeText = "Hello, World")

if __name__ == "__main__":
    app.run(debug=True)