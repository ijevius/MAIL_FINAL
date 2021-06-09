import threading
import settings

from flask import Flask, jsonify, request

app = Flask(__name__)
ID_STORE = {"jevik": 1}


@app.route('/vk_id/<username>', methods=['GET'])
def get_vk_id(username):
    if vk_id := ID_STORE.get(username):
        return jsonify(vk_id=vk_id), 200
    else:
        return jsonify(), 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'OK, exiting'), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0:8083')