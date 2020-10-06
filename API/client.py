import os
import msgpackrpc

client = msgpackrpc.Client(msgpackrpc.Address(os.environ['ns_host'], int(os.environ['ns_port'])))
