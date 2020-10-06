from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from werkzeug.utils import secure_filename
import time
import numpy

UPLOAD_FOLDER = "./attachments"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

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
            "message":"Private Info",
            "indices": [index1, index2]
        },
        {
            "message":"Confidentiality Issue",
            "indices": [index3, index4]
        }
    ]

    return jsonify(reply)

@app.route("/analyzeattachment", methods=['POST'])
def analyze_attachment():
    if 'file' not in request.files:
            abort(400, description="Resource not found")
    file = request.files['file']
    # if user does not select file, browser also submit an empty part without filename
    if file.filename == '':
        abort(400, description="Resource not found")
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.filename = filename
        return jsonify(file)
