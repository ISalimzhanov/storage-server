import argparse
import os
import sys

import requests

from storage_server.storage import Storage

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-ss_host", help="storage server's IPv4 address", type=str)
    parser.add_argument("-ss_port", help="storage server's port", type=str)
    parser.add_argument("-ss_dir", help="path to local storage directory", type=str)
    parser.add_argument('-ss_cap', help='capacity of storage server in bytes', type=str)
    parser.add_argument("-ns_host", help="naming server's IPv4 address", type=str)
    parser.add_argument("-ns_port", help="naming server's port", type=str)
    parser.add_argument("-connector", help="connector to NS server", type=str)

    args = parser.parse_args()
    os.environ['ss_host'] = args.ss_host
    os.environ['ss_port'] = args.ss_port
    os.environ['ss_dir'] = args.ss_dir
    os.environ['ss_cap'] = args.ss_cap
    os.environ['ns_host'] = args.ns_host
    os.environ['ns_port'] = args.ns_port
    connector = args.connector

    from API.server import launch_server
    from API.client import connect, register

    ss = Storage()
    print(ss.clear())

    try:
        try:
            ns_awared = connect(connector)
        except FileNotFoundError:
            ns_awared = register(connector)
        if not ns_awared:
            sys.exit(f'Naming Server {os.environ["ns_host"]} at port {os.environ["ns_port"]} '
                     f'deny registration/connection')
    except requests.exceptions.ConnectionError:
        sys.exit(f'Naming Server {os.environ["ns_host"]} at port {os.environ["ns_port"]} is unavailable')

    launch_server()
