from storage_server.storageServer import StorageServer

if __name__ == '__main__':
    ss = StorageServer('temp')
    operation_desc = {'type': 'smth', 'requester': '0.0.0.0'}
    ss.delete('name/file.txt')
