from storage_server.storage import Storage
import msgpackrpc
import os


class ServerService(object):
    storage = Storage()
    # toDo


server = msgpackrpc.Server(ServerService)
server.listen(msgpackrpc.Address(os.environ['ss_host'], int(os.environ['ss_port'])))
