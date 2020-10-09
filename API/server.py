from threading import Thread
from storage_server.storage import Storage
import msgpackrpc
import os


class ServerService(object):
    def __init__(self):
        self.storage = Storage()

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


def launch_server() -> tuple:
    address = msgpackrpc.Address(os.environ['ss_host'], int(os.environ['ss_port']))
    server = msgpackrpc.Server(ServerService())
    server.listen(address)
    thread = Thread(target=server.start)
    print(f"Server launched at {os.environ['ss_host']} on port {os.environ['ss_port']}")
    thread.start()
    return address, server, thread
