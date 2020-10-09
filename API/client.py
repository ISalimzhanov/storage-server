import os
import msgpackrpc


def register():
    address = msgpackrpc.Address(os.environ['ns_host'], int(os.environ['ns_port']))
    client = msgpackrpc.Client(address, unpack_encoding='utf-8')
    client.call('register')
