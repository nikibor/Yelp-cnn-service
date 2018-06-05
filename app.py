import requests
from flask import Flask, request
import json
import requests as http_requests
from classificator import CNN
from serializer import ClassificationSerializer

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "OK!"


@app.route('/api/cnn', methods=['POST'])
def cnn_classification_debug():
    if request.is_json:
        data = request.get_json()
        serializer = ClassificationSerializer(data=data)
        if not serializer.is_valid():
            return 'Error!'

        data = {
            "text": serializer.text,
            "token": serializer.token
        }
        embeding_response = http_requests.post(url='https://yelp-vector-service.herokuapp.com/api/embedding', json=data)
        vector = embeding_response.json()['vector']
        cnn_classes = CNN().classify(vector=vector).tolist()
        result = {'cnn_classes': cnn_classes}
        return json.dumps(result)


# @app.route('/api/debug/cnn', methods=['POST'])
# def cnn_classification_debug():
#     if request.is_json:
#         data = request.get_json()
#         serializer = ClassificationSerializer(data=data)
#         if serializer.is_valid():
#             vector = serializer.text
#             hashkey = serializer.hashkey
#             cnn_classes = CNN().classify(vector=vector).tolist()
#             result = {'cnn_classes': cnn_classes, 'hashkey': hashkey}
#             requests.post(url='yelp.main.com', json=result)
#     return 'Error!'


if __name__ == '__main__':
    app.run()
