import os
import shutil
from typing import Optional
import json
from storage_server.receipt import Receipt
from queue import Queue
from config import ss_dir


class StorageServer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not StorageServer._instance:
            StorageServer._instance = super(StorageServer, cls).__new__(cls)
        return StorageServer._instance

    def __init__(self):
        self.dir = ss_dir
        try:
            os.mkdir(self.dir)
            self._storage = []
        except FileExistsError:
            self._storage = self.get_receipts()
            if not self.valid_storage(self.dir):
                raise AttributeError

    def get_receipts(self) -> list:
        """
        Get all receipts from storage directory and its subdirectories
        :return: list of receipts
        """
        receipts = []
        q = Queue()
        q.put(self.dir)
        while not q.empty():
            cur_dir = q.get()
            for path in os.listdir(cur_dir):
                storage_path = f'{cur_dir}/{path}'
                if os.path.isdir(storage_path):
                    q.put(storage_path)
                elif storage_path.endswith('.json'):
                    receipts.append(Receipt(storage_path))
        return receipts

    def valid_storage(self, directory: str) -> bool:
        """
        Check if there are any file in the directory and its subdirectories
        For which we don't have a receipt
        :return: False if there are
                 True if there aren't
        """
        for content in os.listdir(directory):
            if os.path.isdir(content):
                self.valid_storage(content)
            elif not content.endswith('.json'):
                if content in self:
                    return False
        return True

    def read(self, path: str, operation_desc: dict) -> bytes:
        if path not in self:
            raise ValueError
        receipt = self[path]
        storage_path = f'{self.dir}/{path}'
        with open(storage_path, 'rb') as file:
            data = file.read()
        receipt.add_operation(operation_desc)
        return data

    def write(self, path: str, data: bytes, operation_desc: dict) -> None:
        if path not in self:
            raise ValueError
        receipt = self[path]
        storage_path = f'{self.dir}/{path}'
        with open(storage_path, 'wb') as file:
            file.write(data)
        receipt.add_operation(operation_desc)

    def build_path(self, path: str) -> None:
        """
        Create directories from the path
        If they don't exist already
        :param path:
        :return:
        """
        dirs: list = path.split('/')[1:-1]
        path_dir = self.dir
        for d in dirs:
            path_dir = f'{path_dir}/{d}'
            if not os.path.isdir(path_dir):
                os.mkdir(path_dir)

    def create(self, path: str, operation_desc: dict) -> None:
        if path in self:
            raise ValueError
        storage_path = f'{self.dir}/{path}'
        self.build_path(storage_path)
        # creating file
        file = open(storage_path, 'w')
        file.close()
        # create json file with metadata
        json_path = storage_path.split(".")[0]
        json_path = f'{json_path}.json'
        with open(json_path, 'w') as jsonfile:
            data = {'path': path, 'operations': [operation_desc]}
            json.dump(data, jsonfile)
        receipt = Receipt(json_path)
        self._storage.append(receipt)

    def clear_path(self, path: str) -> None:
        """
        Delete all empty directories on specific path
        :param path:
        :return:
        """
        dirs: list = path.split('/')[1:-1]  # self.dir should not be cleared
        path_dir = self.dir
        for i in range(len(dirs)):
            path_dir = f'{path_dir}/{dirs[i]}'
            dirs[i] = path_dir
        dirs.reverse()
        for d in dirs:
            if not os.listdir(d):
                os.rmdir(d)
            else:
                break

    def delete(self, path: str) -> None:
        if path not in self:
            raise ValueError
        receipt = self[path]
        storage_path = f'{self.dir}/{path}'
        os.remove(storage_path)
        del self[receipt]
        self.clear_path(storage_path)

    def move(self, src_path: str, dest_path: str, operation_desc: dict) -> None:
        if src_path not in self:
            raise ValueError
        receipt = self[src_path]
        shutil.move(f'{self.dir}/{src_path}', f'{self.dir}/{dest_path}')
        receipt['path'] = dest_path
        receipt.add_operation(operation_desc)

    def ls(self) -> list:
        return [receipt['path'] for receipt in self]

    def __len__(self) -> int:
        return len(self._storage)

    def __contains__(self, path: str) -> bool:
        for i in range(len(self._storage)):
            receipt = self._storage[i]
            if receipt['path'] == path:
                return True
        return False

    def __getitem__(self, path: str) -> Optional[Receipt]:
        for i in range(len(self._storage)):
            receipt = self._storage[i]
            if receipt['path'] == path:
                return receipt
        return None

    def __delitem__(self, receipt: Receipt) -> None:
        receipt.delete()
        self._storage.remove(receipt)
