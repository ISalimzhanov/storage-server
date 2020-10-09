from threading import Thread
from storage_server.storage import Storage
import msgpack
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
    req_body = msgpack.unpackb(request.get_data(), use_list=False)
    ss = ServerService()
    result = None
    try:
        if req_body['method'] == 'ping':
            ss.ping()
        elif req_body['method'] == 'init':
            result = {'spaceAvailable': ss.init()}
        elif req_body['method'] == 'create':
            ss.create(req_body['params']['id'])
        elif req_body['method'] == 'write':
            ss.create(req_body['params']['id'])
        elif req_body['method'] == 'read':
            result = {'contents': ss.create(req_body['params']['id'])}
        elif req_body['method'] == 'delete':
            ss.delete(req_body['params']['id'])
        response = {'jsonrpc': '2.0', 'result': result, 'success': True, 'type': req_body['method']}
    except Exception:
        response = {'jsonrpc': '2.0', 'error': 'something went wrong', 'success': False, 'type': req_body['method']}
    return Response(msgpack.packb(response), 200, content_type='application/msgpack')


def launch_server() -> tuple:
    thread = Thread(target=app.run, args=(os.environ['ss_host'], os.environ['ss_port']))
    print(f"Server launched at {os.environ['ss_host']} on port {os.environ['ss_port']}")
    thread.start()
    return app, thread
