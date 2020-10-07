from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from werkzeug.utils import secure_filename
import time
import numpy
#import os


#Globals
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
    subject = data['subject']

    print(subject, text)

    #Your Input are the variables "text" and "subject"

    Output = None  #Call Model Here

    """
    Format Output Like This:
    (List of Dictionaries, each of which have a message key for a text value and an indices key for a list of 2 indices)

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
    """

    return jsonify(Output)


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
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))    #Enable this to save in attachments folder
        data = file.read()          #This is the data you need to process my friend
        return jsonify("Issue")     #Send Better Outputs

    abort(400, description="Resource not found")

