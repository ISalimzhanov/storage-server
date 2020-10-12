import msgpack
import requests
from requests import Response
import os


def register(connector: str) -> bool:
    req = {'jsonrpc': '2.0', 'method': 'replica.register', 'params': {'connector': connector}}
    req_data = msgpack.packb(req)
    response: Response = requests.post(f'http://{os.environ["ns_host"]}:{os.environ["ns_port"]}/api/replica',
                                       data=req_data, headers={'content-type': 'application/msgpack'})
    response_data = msgpack.unpackb(response.content)
    if response_data['success']:
        with open('id', 'w') as file:
            file.write(response_data['result']['id'])
        return True
    return False


def connect(connector: str) -> bool:
    with open('id', 'r') as file:
        id = file.read()
    req = {'jsonrpc': '2.0', 'method': 'replica.connect', 'params': {'id': id, 'connector': connector}}
    req_data = msgpack.packb(req)
    response: Response = requests.post(f'http://{os.environ["ns_host"]}:{os.environ["ns_port"]}/api/replica',
                                       data=req_data, headers={'content-type': 'application/msgpack'})
    response_data = msgpack.unpackb(response.content)
    return response_data['success']
