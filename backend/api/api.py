from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import numpy

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def test():
    return "Hello World!"

@app.route("/analyze", methods=['POST'])
def analyze():
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