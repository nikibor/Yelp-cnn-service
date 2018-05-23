import requests
from flask import Flask, request
import json
from classificator import CNN
from serializer import ClassificationSerializer

app = Flask(__name__)


@app.route('/api/debug/cnn', methods=['POST'])
def cnn_classification_debug():
    if request.is_json:
        data = request.get_json()
        serializer = ClassificationSerializer(data=data)
        if serializer.is_valid():
            vector = serializer.vector
            cnn_classes = CNN().classify(vector=vector).tolist()
            result = {'cnn_classes': cnn_classes}
            return json.dumps(result)
    return 'Error!'


@app.route('/api/debug/cnn', methods=['POST'])
def cnn_classification_debug():
    if request.is_json:
        data = request.get_json()
        serializer = ClassificationSerializer(data=data)
        if serializer.is_valid():
            vector = serializer.vector
            hashkey = serializer.hashkey
            cnn_classes = CNN().classify(vector=vector).tolist()
            result = {'cnn_classes': cnn_classes, 'hashkey': hashkey}
            requests.post(url='yelp.main.com', json=result)
    return 'Error!'


if __name__ == '__main__':
    app.run()
