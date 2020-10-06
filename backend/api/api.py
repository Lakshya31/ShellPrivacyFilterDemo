from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import numpy

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def test():
    return "Hello World!"

@app.route("/analyzetext", methods=['POST'])
def analyze_text():
    data = request.get_json()
    text = data['text']

    #Your Input is the variable "text"

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

# @app.route("/analyzeattachment", methods=['POST'])
# def analyze_attachment():

