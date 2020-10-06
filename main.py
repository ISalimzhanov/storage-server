import argparse
import os
from threading import Thread
from config import ns_host, ns_port

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s_host", help="server's address", type=str)
    parser.add_argument("-s_port", help="server's port", type=int)
    args = parser.parse_args()
    os.environ['s_host'] = args.s_host
    os.environ['s_port'] = str(args.s_port)
    os.environ['ns_host'] = ns_host  # toDo
    os.environ['ns_port'] = str(ns_port)  # toDo

    from API.client import client
    from API.server import server

    # client.call('register')

    thread = Thread(target=server.start)
    print('Server launched')
    thread.start()
