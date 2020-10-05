import argparse
import os
from threading import Thread
from API.client import Client
from API.server import Server
from config import ns_host, ns_port

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s_host", help="server's address", type=str)
    parser.add_argument("-s_port", help="server's port", type=int)
    args = parser.parse_args()
    os.environ['s_host'] = args.s_host
    os.environ['s_port'] = str(args.s_port)
    os.environ['ns_host'] = ns_host  # toDo
    os.environ['ns_port'] = ns_port  # toDo

    server = Server()
    thread = Thread(target=server.launch)
    print('Server launched')
    thread.start()

    # client = Client() toDO
    # client.register() toDo
