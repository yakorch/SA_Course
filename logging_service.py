from service_addresses import *

from flask import Flask, request, jsonify

app = Flask(__name__)

logged_messages = {}


@app.route(LOGGING_SERVICE.POST_suffix, methods=['POST'])
def log_message():
    data = request.json
    logged_messages[data['id']] = data['msg']

    return jsonify({"status": "Message logged"}), 200


@app.route(LOGGING_SERVICE.GET_suffix, methods=['GET'])
def get_messages():
    all_messages = list(logged_messages.values())
    return jsonify(all_messages), 200


if __name__ == '__main__':
    app.run(port=LOGGING_SERVICE.port)
