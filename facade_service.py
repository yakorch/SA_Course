from service_addresses import *

import uuid

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route(FACADE_SERVICE.POST_suffix, methods=['POST'])
def post_message():
    msg = request.json['msg']
    message_id = str(uuid.uuid4())

    print(f"Received message: {msg} with ID: {message_id}")

    requests.post(LOGGING_SERVICE.get_POST_endpoint(), json={'id': message_id, 'msg': msg})
    return jsonify({'message_id': message_id}), 200


@app.route(FACADE_SERVICE.GET_suffix, methods=['GET'])
def get_messages():

    logs = requests.get(LOGGING_SERVICE.get_GET_endpoint()).text

    static_message = requests.get(STATIC_SERVICE.get_GET_endpoint()).text
    return logs + '\n' + static_message, 200


if __name__ == '__main__':
    app.run(port=FACADE_SERVICE.port)
