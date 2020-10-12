import msgpack
import requests
import os


def register(connector: str) -> bool:
    req = {'jsonrpc': '2.0', 'method': 'replica.register', 'params': {'connector': connector}}
    req_data = msgpack.packb(req)
    response_data = requests.post(f'http://{os.environ["ns_host"]}:{os.environ["ns_port"]}/api/replica', data=req_data)
    response = msgpack.unpackb(response_data)
    if response['success']:
        with open('id', 'w') as file:
            file.write(response['id'])
        return True
    return False


def connect() -> bool:
    with open('id', 'r') as file:
        id = file.read()
    req = {'jsonrpc': '2.0', 'method': 'replica.register', 'params': {'id': id}}
    req_data = msgpack.packb(req)
    response_data = requests.post(f'http://{os.environ["ns_host"]}:{os.environ["ns_port"]}/api/replica', data=req_data)
    response = msgpack.unpackb(response_data)
    return response['success']
