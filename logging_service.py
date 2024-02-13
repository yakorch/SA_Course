from service_addresses import *

from flask import Flask, request, jsonify

app = Flask(__name__)

logged_messages = {}


@app.route(LOGGING_SERVICE.POST_suffix, methods=['POST'])
def log_message():
    data = request.json
    logged_messages[data['id']] = data['msg']

    print(f"Logged message: {data['msg']} with ID: {data['id']}")
    return jsonify({"status": "Message logged"}), 200


@app.route(LOGGING_SERVICE.GET_suffix, methods=['GET'])
def get_messages():
    # Concatenate all messages stored in memory
    all_messages = '\n'.join(logged_messages.values())
    return all_messages, 200


if __name__ == '__main__':
    app.run(port=LOGGING_SERVICE.port)
