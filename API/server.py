from storage_server.receipt import Receipt
from storage_server.storageServer import StorageServer
import msgpackrpc
import os


class ServerService(object):
    storage_server = StorageServer()

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

    def ping(self):
        return True


server = msgpackrpc.Server(ServerService)
server.listen(msgpackrpc.Address(os.environ['s_host'], int(os.environ['s_port'])))
