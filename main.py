import argparse
import os
from threading import Thread

from storage_server.storage import Storage

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-ss_host", help="storage server's IPv4 address", type=str)
    parser.add_argument("-ss_port", help="storage server's port", type=int)
    parser.add_argument("-ss_dir", help="path to local storage directory", type=str)
    parser.add_argument("-ns_host", help="naming server's IPv4 address", type=str)
    parser.add_argument("-ns_port", help="naming server's port", type=int)
    args = parser.parse_args()
    os.environ['ss_host'] = args.ss_host
    os.environ['ss_port'] = str(args.ss_port)
    os.environ['ss_dir'] = args.ss_dir
    os.environ['ns_host'] = args.ns_host
    os.environ['ns_port'] = str(args.ns_port)

    from API.client import client
    from API.server import server

    # client.call('register') toDO

    thread = Thread(target=server.start)
    print('Server launched')
    thread.start()
