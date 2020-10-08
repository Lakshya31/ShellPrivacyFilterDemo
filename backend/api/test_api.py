from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from werkzeug.utils import secure_filename
import time
import numpy
#import os

UPLOAD_FOLDER = "./attachments"
ALLOWED_EXTENSIONS = {'docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

#Extension_Check
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=['GET'])
def test():
    return "Hello World!"


@app.route("/analyzetext", methods=['POST'])
def analyze_text():
    data = request.get_json()
    text = data['text']
    print(text)

    if len(text) < 10:
        return jsonify([])

    index1 = numpy.random.randint(0,len(text)//4)
    index2 = numpy.random.randint(len(text)//4,len(text)//2)
    index3 = numpy.random.randint(len(text)//2,len(text)//4*3)
    index4 = numpy.random.randint(len(text)//4*3,len(text))

    reply = [
        {
            "message":"Violation of Privacy Policy",
            "indices": [index1, index2]
        },
        {
            "message":"Breach of Confidentiality",
            "indices": [index3, index4]
        }
    ]

    return jsonify(reply)


@app.route("/analyzeattachment", methods=['POST'])
def analyze_attachment():

    if 'file' not in request.files:
        print("No File")
        abort(400, description="Resource not found")

    file = request.files['file']
    if file.filename == '':
        print("No File Name")
        abort(400, description="Resource not found")

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.filename = filename
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        data = file.read()
        return jsonify("issue")

    abort(400, description="Resource not found")
