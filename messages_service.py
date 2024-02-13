from service_addresses import *

from flask import Flask, jsonify

app = Flask(__name__)


@app.route(STATIC_SERVICE.GET_suffix, methods=['GET'])
def get_static_message():
    return jsonify({"message": "Service not implemented yet"}), 200


if __name__ == '__main__':
    app.run(port=STATIC_SERVICE.port)
