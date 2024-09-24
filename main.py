from flask import Flask
from flask import render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from image_converter import ImageConverter
import os

FILE_FORMAT = ['PNG', 'JPG', 'JPEG', 'ICO', 'WEBP']
UPLOAD_FOLDER = './app/uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/home')
@app.route('/')
def main():
    app.logger.info("Loading home page... ")
    return render_template('index.html', file_format=FILE_FORMAT,  output_file=None)

@app.route('/home', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def convert():
    if request.method == 'POST':
        app.logger.info("The file converter function action... ")
        
        # Get the form values
        file_path = request.files['file-path']
        toConvert = request.form['file-format']

        upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file_path.filename))

        # Save the file
        file_path.save(upload_file_path)
        app.logger.info("The file uploaded to the cloud....")

        # Converter Porcess
        output_file = ImageConverter(upload_file_path, toConvert).convert()
        app.logger.info("The file was converted into new format... ")

        list_val = output_file.split('/')
        list_val.pop(0)
        output_file = "/".join(list_val)

        return render_template('index.html', file_format=FILE_FORMAT,  output_file=output_file)
    return redirect(url_for('main'))

@app.route('/app/uploads/<filename>')
def download_file(filename):
    app.logger.info("file send to download.... ")
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)