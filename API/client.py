import msgpack
import requests
import os
from flask import Response


def register(connector: str) -> bool:
    req = {'jsonrpc': '2.0', 'method': 'replica.register', 'params': {'connector': connector}}
    req_data = msgpack.packb(req)
    response: Response = requests.post(f'http://{os.environ["ns_host"]}:{os.environ["ns_port"]}/api/replica',
                                       data=req_data, headers={'content-type': 'application/msgpack'})
    response_data = msgpack.unpackb(response.get_data())
    if response_data['success']:
        with open('id', 'w') as file:
            file.write(response_data['id'])
        return True
    return False


def connect() -> bool:
    with open('id', 'r') as file:
        id = file.read()
    req = {'jsonrpc': '2.0', 'method': 'replica.register', 'params': {'id': id}}
    req_data = msgpack.packb(req)
    response: Response = requests.post(f'http://{os.environ["ns_host"]}:{os.environ["ns_port"]}/api/replica',
                                       data=req_data, headers={'content-type': 'application/msgpack'})
    response_data = msgpack.unpackb(response.get_data())
    return response_data['success']
