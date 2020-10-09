from threading import Thread
from storage_server.storage import Storage
from flask import Flask, request, Response
import os

app = Flask(__name__)


class ServerService(object):
    storage = Storage()

    def ping(self) -> None:
        return None

    def init(self) -> int:
        return self.storage.available_space()

    def create(self, id: bytes) -> None:
        path = id.decode('utf-8')
        self.storage.create(path)

    def write(self, id: bytes, content: bytes) -> None:
        path = id.decode('utf-8')
        self.storage.write(path, content)

    def read(self, id: bytes) -> bytes:
        path = id.decode('utf-8')
        return self.storage.read(path)

    def delete(self, ids: list) -> None:
        for id in ids:
            if type(id) != bytes:
                raise ValueError
        for id in ids:
            path = id.decode('utf-8')
            self.storage.delete(path)


@app.route('/', methods=['POST'])
def handler():
    req = request.get_data().decode('utf-8')
    ss = ServerService()
    switch_map = {
        'ping': lambda x: x.ping(),
        'init': lambda x: x.init(),
        'create': lambda x, id: x.create(id),
        'write': lambda x, id, content: x.write(id, content),
        'read': lambda x, id: x.read(id),
        'delete': lambda x, id: x.delete(id)
    }
    result = None
    try:
        if req['method'] == 'ping':
            result = ss.ping()
        elif req['method'] == 'init':
            result = ss.init()
        elif req['method'] == 'create':
            result = ss.create(req['params']['id'])
        elif req['method'] == 'write':
            result = ss.create(req['params']['id'])
        elif req['method'] == 'read':
            result = ss.create(req['params']['id'])
        elif req['method'] == 'delete':
            result = ss.delete(req['params']['id'])
        response = {'jsonrpc': '2.0', 'result': result, 'success': True}
    except Exception:
        response = {'jsonrpc': '2.0', 'error': 'something went wrong', 'success': False}
    return Response(response, 200)


def launch_server() -> tuple:
    thread = Thread(target=app.run, args=(os.environ['ss_host'], os.environ['ss_port']))
    print(f"Server launched at {os.environ['ss_host']} on port {os.environ['ss_port']}")
    thread.start()
    return app, thread
