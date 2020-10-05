import socket
from bsonrpc import JSONRpc
import os


class Client:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not Client._instance:
            Client._instance = super(Client, cls).__new__(cls)
        return Client._instance

    def __init__(self):
        # Cut-the-corners TCP Client:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((os.environ['ns_host'], os.environ['ns_port']))
        self.rpc = JSONRpc(self.socket)
        self.server = self.rpc.get_peer_proxy()

    def register(self):
        self.server.register()
