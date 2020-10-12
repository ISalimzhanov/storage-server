import os
import shutil
import sys
from queue import Queue


class Storage:
    """
    Singleton class that implement
    Structured File Storage (directories) support
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not Storage._instance:
            Storage._instance = super(Storage, cls).__new__(cls)
        return Storage._instance

    def __init__(self):
        """
        self.__dir - root directory of the storage
        self.__cap - capacity at the moment
        self.__content - list of DFS paths in the root directory and its sub directories,
        """
        self.__dir = os.environ['ss_dir']
        self.__cap = int(os.environ['ss_cap'])
        try:
            os.mkdir(self.__dir)
            self.__content = []
        except FileExistsError:
            self.__content, size = self.__get_info()
            if self.__cap < size:
                raise AttributeError
            self.__cap -= size

    def __len__(self) -> int:
        """
        :return: currently available space in storage
        """
        return self.__cap

    def __contains__(self, path: str) -> bool:
        """
        :param path: some DFS path
        :return: True - entity with such path exists in DFS
                 False - entity with such path doesn't exist in DFS
        """
        try:
            self.__content.index(path)
            return True
        except ValueError:
            return False

    def __iter__(self):
        """
        :return:
        """
        return self.__content.__iter__()

    def __getitem__(self, path: str):
        """
        :param path: DFS path to file
        :return: data in the file with such path
        """
        if path not in self:
            raise FileNotFoundError
        storage_path = f'{self.__dir}/{path}'
        with open(storage_path, 'rb') as file:
            data = file.read()
        return data

    def __setitem__(self, path: str, data: bytes) -> None:
        """
        Create file filled by the data
        :param path: DFS path to file
        :param data: data in byte format
        :return:
        """
        if path in self:
            raise FileExistsError
        if self.__cap < sys.getsizeof(data):
            raise OSError
        self.__cap -= sys.getsizeof(data)
        storage_path = f'{self.__dir}/{path}'
        self.__build_path(storage_path)
        with open(storage_path, 'wb') as file:
            file.write(data)
        self.__content.append(path)

    def __delitem__(self, path: str) -> None:
        """
        Delete file
        :param path: DFS path to a file
        :return:
        """
        if path not in self:
            raise FileNotFoundError
        storage_path = f'{self.__dir}/{path}'
        self.__cap += os.path.getsize(storage_path)
        os.remove(storage_path)
        self.__clear_path(storage_path)
        self.__content.remove(path)

    def __get_info(self) -> tuple:
        """
        :return: (list of DFS filenames, size occupied)
        """
        fnames = []
        size = 0
        q = Queue()
        for path in os.listdir(self.__dir):
            storage_path = f'{self.__dir}/{path}'
            if os.path.isdir(storage_path):
                q.put(path)
            else:
                fnames.append(path)
                size += os.path.getsize(storage_path)
        while not q.empty():
            dfs_dir = q.get()  # dfs path to current directory
            storage_dir = f'{self.__dir}/{dfs_dir}'  # storage path to current directory
            for path in os.listdir(storage_dir):
                dfs_path = f'{dfs_dir}/{path}'
                if os.path.isdir(dfs_path):
                    q.put(dfs_path)
                else:
                    fnames.append(dfs_path)
                    size += os.path.getsize(dfs_path)
        return fnames, size

    def __build_path(self, storage_path: str) -> None:
        """
        Create directories from the path
        If they don't exist already
        :param storage_path: full path to file
        :return:
        """
        dirs: list = storage_path.split('/')[1:-1]
        path_dir = self.__dir  # path to directory
        for d in dirs:
            path_dir = f'{path_dir}/{d}'
            if not os.path.isdir(path_dir):
                os.mkdir(path_dir)

    def __clear_path(self, path: str) -> None:
        """
        Delete all empty directories on specific path
        :param path:
        :return:
        """
        dirs: list = path.split('/')[1:-1]  # self.dir should not be deleted
        path_dir = self.__dir  # path from storage directory
        for i in range(len(dirs)):
            path_dir = f'{path_dir}/{dirs[i]}'
            dirs[i] = path_dir
        dirs.reverse()
        for d in dirs:
            if not os.listdir(d):
                os.rmdir(d)
            else:
                break

    def move(self, src_path: str, dest_path: str) -> None:
        """
        :param src_path: DFS initial path to file
        :param dest_path: DFS path to where path should be located
        :return:
        """
        if src_path not in self:
            raise FileNotFoundError
        dest_storage_path = f'{self.__dir}/{dest_path}'
        src_storage_path = f'{self.__dir}/{src_path}'
        self.__build_path(dest_storage_path)
        shutil.move(src_storage_path, dest_storage_path)
        self.__clear_path(src_storage_path)

        ind = self.__content.index(src_path)
        self.__content[ind] = dest_path  # updating self.__content

    def ls(self) -> list:
        """
        :return: list of DFS filenames
        """
        return [fname for fname in self]

    def clear(self) -> None:
        """
        Clear storage
        :return:
        """
        shutil.rmtree(self.__dir)
        self.__cap = os.environ['ss_cap']
        os.mkdir(self.__dir)
        self.__content = []
