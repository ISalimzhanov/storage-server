import os
import shutil
import sys
from queue import Queue


class Storage:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not Storage._instance:
            Storage._instance = super(Storage, cls).__new__(cls)
        return Storage._instance

    def __init__(self):
        self.dir = os.environ['ss_dir']
        self.__cap = int(os.environ['ss_cap'])
        try:
            os.mkdir(self.dir)
            self.__content = []
        except FileExistsError:
            self.__content, size = self.__get_info()
            if self.__cap < size:
                raise AttributeError
            self.__cap -= size

    def __len__(self) -> int:
        return len(self.__content)

    def __contains__(self, path: str) -> bool:
        try:
            self.__content.index(path)
            return True
        except ValueError:
            return False

    def __iter__(self):
        return self.__content.__iter__()

    def __setitem__(self, src_path: str, dest_path: str) -> None:
        idx = self.__content.index(src_path)
        self.__content[idx] = dest_path

    def __delitem__(self, path: str) -> None:
        self.__content.remove(path)

    def __get_info(self) -> tuple:
        """
        :return: (list of filenames, size occupied)
        """
        fnames = []
        size = 0
        q = Queue()
        for path in os.listdir(self.dir):
            storage_path = f'{self.dir}/{path}'
            if os.path.isdir(storage_path):
                q.put(path)
            else:
                fnames.append(path)
                size += os.path.getsize(storage_path)
        while not q.empty():
            dfs_dir = q.get()  # dfs path to current directory
            storage_dir = f'{self.dir}/{dfs_dir}'  # storage path to current directory
            for path in os.listdir(storage_dir):
                dfs_path = f'{dfs_dir}/{path}'
                if os.path.isdir(dfs_path):
                    q.put(dfs_path)
                else:
                    fnames.append(dfs_path)
                    size += os.path.getsize(dfs_path)
        return fnames, size

    def read(self, path: str) -> bytes:
        if path not in self:
            raise FileNotFoundError
        storage_path = f'{self.dir}/{path}'
        with open(storage_path, 'rb') as file:
            data = file.read()
        return data

    def write(self, path: str, data: bytes) -> None:
        if path in self:
            raise FileExistsError
        if self.__cap < sys.getsizeof(data):
            raise OSError
        self.__cap -= sys.getsizeof(data)
        storage_path = f'{self.dir}/{path}'
        with open(storage_path, 'wb') as file:
            file.write(data)
        self.__content.append(path)

    def build_path(self, storage_path: str) -> None:
        """
        Create directories from the path
        If they don't exist already
        :param storage_path: full path to file
        :return:
        """
        dirs: list = storage_path.split('/')[1:-1]
        path_dir = self.dir  # path to directory
        for d in dirs:
            path_dir = f'{path_dir}/{d}'
            if not os.path.isdir(path_dir):
                os.mkdir(path_dir)

    def create(self, path: str) -> None:
        if path in self:
            raise FileExistsError
        storage_path = f'{self.dir}/{path}'
        self.build_path(storage_path)
        file = open(storage_path, 'w')
        file.close()
        self.__content.append(path)

    def clear_path(self, path: str) -> None:
        """
        Delete all empty directories on specific path
        :param path:
        :return:
        """
        dirs: list = path.split('/')[1:-1]  # self.dir should not be deleted
        path_dir = self.dir  # path from storage directory
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
            raise FileNotFoundError
        storage_path = f'{self.dir}/{path}'
        self.__cap += os.path.getsize(storage_path)
        del self[path]
        os.remove(storage_path)
        self.clear_path(storage_path)

    def move(self, src_path: str, dest_path: str) -> None:
        if src_path not in self:
            raise FileNotFoundError
        dest_storage_path = f'{self.dir}/{dest_path}'
        src_storage_path = f'{self.dir}/{src_path}'
        self.build_path(dest_storage_path)
        shutil.move(src_storage_path, dest_storage_path)
        self[src_path] = dest_path
        self.clear_path(src_storage_path)

    def ls(self) -> list:
        return [fname for fname in self]

    def available_space(self) -> int:
        return self.__cap
