from threading import Thread
from storage.storage import Storage
import os
from API import storageService_pb2, storageService_pb2_grpc
import grpc
from concurrent import futures
import logging


class StorageService(storageService_pb2_grpc.StorageServiceServicer):
    """
    Class which defines server services
    Storage, which assigned to Storage Server
    Is Flat (do work with directories)
    It, actually, works with files ID
    In the Naming Server's database
    Providing ids is the job of NS
    """
    _storage = Storage()

    def Ping(self, request, context):
        return storageService_pb2.ControlReply(success=True)

    def Clear(self, request, context):
        self._storage.clear()
        return storageService_pb2.ControlReply(success=True)

    def Create(self, request, context):
        try:
            self._storage[request.filename] = b''
            return storageService_pb2.UpdateReply(success=True, capacity=len(self._storage))
        except FileExistsError as error:
            return storageService_pb2.UpdateReply(success=False, error=error)
        except OSError:
            return storageService_pb2.UpdateReply(success=False, error='Not enough space')

    def Write(self, request, context):
        try:
            self._storage[request.filename] = request.data
            return storageService_pb2.UpdateReply(success=True, capacity=len(self._storage))
        except FileExistsError as error:
            return storageService_pb2.UpdateReply(success=False, error=error)
        except OSError:
            return storageService_pb2.UpdateReply(success=False, error='Not enough space')

    def Read(self, request, context):
        try:
            data = self._storage[request.filename]
            return storageService_pb2.UpdateReply(success=True, data=data)
        except FileNotFoundError as error:
            return storageService_pb2.UpdateReply(success=False, error=error)

    def Delete(self, request, context):
        try:
            for fname in request.filenames:
                del self._storage[fname]
            return storageService_pb2.UpdateReply(success=True)
        except FileNotFoundError as error:
            return storageService_pb2.UpdateReply(success=False, error=error)


def serve(server, port: int):
    storageService_pb2_grpc.add_StorageServiceServicer_to_server(StorageService(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()


def launch_server() -> tuple:
    """
    :return: thread where server running, Flask's app
    """
    logging.basicConfig()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    thread = Thread(target=serve, args=(server, os.environ['ss_port']))
    print(f"Server launched at localhost on port {os.environ['ss_port']}")
    thread.start()
    return server, thread
