import os
import shutil
from queue import Queue


class Storage:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not Storage._instance:
            Storage._instance = super(Storage, cls).__new__(cls)
        return Storage._instance

    def __init__(self):
        self.dir = os.environ['ss_dir']
        try:
            os.mkdir(self.dir)
            self._content = []
        except FileExistsError:
            self._content = self.__get_files()

    def __len__(self) -> int:
        return len(self._content)

    def __contains__(self, path: str) -> bool:
        try:
            self._content.index(path)
            return True
        except ValueError:
            return False

    def __getitem__(self, path: str) -> str:
        idx = self._content.index(path)
        return self._content[idx]

    def __iter__(self):
        return self._content.__iter__()

    def __setitem__(self, src_path: str, dest_path: str) -> None:
        idx = self._content.index(src_path)
        self._content[idx] = dest_path

    def __delitem__(self, path: str) -> None:
        self._content.remove(path)

    def __get_files(self) -> list:
        """
        Get all filenames from storage
        :return: list of filenames
        """
        fnames = []
        q = Queue()
        for path in os.listdir(self.dir):
            storage_path = f'{self.dir}/{path}'
            if os.path.isdir(storage_path):
                q.put(path)
            else:
                fnames.append(path)
        while not q.empty():
            dfs_dir = q.get()  # dfs path to current directory
            storage_dir = f'{self.dir}/{dfs_dir}'  # storage path to current directory
            for path in os.listdir(storage_dir):
                dfs_path = f'{dfs_dir}/{path}'
                if os.path.isdir(dfs_path):
                    q.put(dfs_path)
                else:
                    fnames.append(dfs_path)
        return fnames

    def read(self, path: str) -> bytes:
        if path not in self:
            raise ValueError
        storage_path = f'{self.dir}/{path}'
        with open(storage_path, 'rb') as file:
            data = file.read()
        return data

    def write(self, path: str, data: bytes) -> None:
        if path in self:
            raise ValueError
        storage_path = f'{self.dir}/{path}'
        with open(storage_path, 'wb') as file:
            file.write(data)
        self._content.append(path)

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
            raise ValueError
        storage_path = f'{self.dir}/{path}'
        self.build_path(storage_path)
        file = open(storage_path, 'w')
        file.close()
        self._content.append(path)

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
            raise ValueError
        storage_path = f'{self.dir}/{path}'
        os.remove(storage_path)
        del self[path]
        self.clear_path(storage_path)

    def move(self, src_path: str, dest_path: str) -> None:
        if src_path not in self:
            raise ValueError
        dest_storage_path = f'{self.dir}/{dest_path}'
        src_storage_path = f'{self.dir}/{src_path}'
        self.build_path(dest_storage_path)
        shutil.move(src_storage_path, dest_storage_path)
        self[src_path] = dest_path
        self.clear_path(src_storage_path)

    def ls(self) -> list:
        return [fname for fname in self]

    def file_size(self, path: str) -> int:
        if path not in self:
            raise ValueError
        storage_path = f'{self.dir}/{path}'
        return os.path.getsize(storage_path)
