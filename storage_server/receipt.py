import json
import os


class Receipt:
    def __init__(self, json_path: str):
        if not Receipt.check_json(json_path):
            raise AttributeError
        self.json_path = json_path
        with open(json_path, 'r') as jsonfile:
            self._metadata = json.load(jsonfile)

    def __getitem__(self, key: str):
        return self._metadata[key]

    def __setitem__(self, key, value):
        if key not in self._metadata:
            raise ValueError
        self._metadata[key] = value

    @staticmethod
    def check_operation(operation_desc: dict) -> bool:
        try:
            if type(operation_desc['type']) != str or type(operation_desc['requester']) != str:
                return False
            return True
        except KeyError:
            return False

    @staticmethod
    def check_json(json_path: str) -> bool:
        if json_path.split('.')[1] != 'json':
            return False
        with open(json_path, 'r') as jsonfile:
            data = json.load(jsonfile)
            try:
                if type(data['path']) != str or type(data['operations']) != list:
                    return False
                for operation_desc in data['operations']:
                    if type(operation_desc) != dict:
                        return False
                    if not Receipt.check_operation(operation_desc):
                        return False
                return True
            except KeyError:
                return False

    def add_operation(self, operation_desc: dict) -> None:
        if not Receipt.check_operation(operation_desc):
            raise ValueError
        with open(self.json_path, 'w') as jsonfile:
            self._metadata['operations'].append(operation_desc)
            json.dump(self._metadata, jsonfile)

    def delete(self) -> None:
        os.remove(self.json_path)
        self._metadata = None
        self.json_path = None
