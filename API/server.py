import socket
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from storage_server.receipt import Receipt
from storage_server.storageServer import StorageServer
import os


@service_class
class ServerService:
    storage_server = StorageServer()

    @request
    def handle_operation(self, operation_desc: dict, **kwargs):
        if not Receipt.check_operation(operation_desc):
            raise ValueError
        switch_map = {
            'reading': lambda x: x.read(operation_desc=operation_desc, **kwargs),
            'writing': lambda x: x.write(operation_desc=operation_desc, **kwargs),
            'creation': lambda x: x.create(operation_desc=operation_desc, **kwargs),
            'deletion': lambda x: x.delete(**kwargs),
            'moving': lambda x: x.move(operation_desc=operation_desc, **kwargs),
            'listing': lambda x: x.ls(**kwargs),
            'get_info': lambda x: x[kwargs.get('path')]
        }
        switch_map[operation_desc['type']](ServerService.storage_server)

    @request
    def ping(self):
        return True


class Server:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not Server._instance:
            Server._instance = super(Server, cls).__new__(cls)
        return Server._instance

    def __init__(self):
        self.host = os.environ['s_host']
        self.port = int(os.environ['s_port'])
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))

    def launch(self):
        self.socket.listen(10)
        while True:
            conn, address = self.socket.accept()
            JSONRpc(conn, Server())
