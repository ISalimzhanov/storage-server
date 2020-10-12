import argparse
import os
import time

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

    timeout = 20
    ns_awared = False  # is NS server about the fact that this SS server is launched
    while not ns_awared:
        try:
            ns_awared = connect()
        except FileNotFoundError:
            ns_awared = register(connector)
        time.sleep(timeout)

    launch_server()
