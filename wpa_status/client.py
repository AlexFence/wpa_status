import socket
import bson
from wpa_status.protocol import Request, Response


class Client():
    def __init__(self, address):
        self._address = address

    def create_socket(self):
        self._socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._socket.connect(self._address)

    def request(self, method, params=None):
        # TODO try to reuse socket
        self.create_socket()
        request = Request(method, params)
        request_bytes = bson.encode(request.serialize())
        self._socket.sendall(request_bytes)

        response_bytes = self._socket.recv(4096 * 2)
        response_bson = bson.decode(response_bytes)
        return Response(response_bson)
