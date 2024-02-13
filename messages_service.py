from service_addresses import *

from flask import Flask

app = Flask(__name__)


@app.route(STATIC_SERVICE.GET_suffix, methods=['GET'])
def get_static_message():
    return "Boring response from the static service", 200


if __name__ == '__main__':
    app.run(port=STATIC_SERVICE.port)
