from flask import Flask
from flask import render_template, request, redirect, url_for
from image_converter import ImageConverter

FILE_FORMAT = ['PNG', 'JPG', 'JPEG', 'ICO', 'WEBP']
UPLOAD_FOLDER = '/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/home')
@app.route('/')
def main():
    app.logger.info("Loading home page... ")
    return render_template('index.html', file_format=FILE_FORMAT)

@app.route('/home', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def convert():
    if request.method == 'POST':
        app.logger.info("The file converter function action... ")
        file_path = request.files['file-path']
        toConvert = request.form['file-format']
        file_path.save()
        return redirect(url_for('main'))
    return render_template('index.html', file_format=FILE_FORMAT)

if __name__ == "__main__":
    app.run(debug=True)