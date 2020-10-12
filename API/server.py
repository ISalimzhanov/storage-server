from threading import Thread
from storage.storage import Storage
import msgpack
from flask import Flask, request, Response
import os

app = Flask(__name__)


class ServerService:
    """
    Class which defines server services
    Storage, which assigned to Storage Server
    Is Flat (do work with directories)
    It, actually, works with files ID
    In the Naming Server's database
    Providing ids is the job of NS
    """
    _storage = Storage()

    def ping(self) -> None:
        """
        :return:
        """
        return None

    def init(self) -> int:
        """
        Clear storage
        :return: available size in clear storage
        """
        self._storage.clear()
        return len(self._storage)

    def create(self, id: str) -> None:
        """
        Create empty file
        :param id: file id in NS's database
        :return:
        """
        self._storage[id] = b''

    def write(self, id: str, contents: bytes) -> None:
        """
        Create file by the data
        :param id: file id in NS's database
        :param contents: data in byte format
        :return:
        """
        self._storage[id] = contents

    def read(self, id: str) -> bytes:
        """
        :param id: file id in NS's database
        :return: data inside file
        """
        return self._storage[id]

    def delete(self, ids: list) -> None:
        """
        :param ids: files ids in NS's database
        :return:
        """
        for id in ids:
            if type(id) != str:
                raise ValueError
        for id in ids:
            del self._storage[id]


@app.route('/', methods=['POST'])
def handler():
    """
    Stub and marshalling of MsgpackRPC
    :return: MsgpackRPC Response
    """
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
            ss.write(req_body['params']['id'], req_body['params']['contents'])
        elif req_body['method'] == 'read':
            result = {'contents': ss.read(req_body['params']['id'])}
        elif req_body['method'] == 'delete':
            ss.delete(req_body['params']['ids'])
        response = {'jsonrpc': '2.0', 'result': result, 'success': True, 'type': req_body['method']}
    except Exception:
        response = {'jsonrpc': '2.0', 'error': 'something went wrong', 'success': False, 'type': req_body['method']}
    return Response(msgpack.packb(response), 200, content_type='application/msgpack')


def launch_server() -> tuple:
    """
    :return: thread where server running, Flask's app
    """
    thread = Thread(target=app.run, args=(os.environ['ss_host'], os.environ['ss_port']))
    print(f"Server launched at {os.environ['ss_host']} on port {os.environ['ss_port']}")
    thread.start()
    return app, thread
