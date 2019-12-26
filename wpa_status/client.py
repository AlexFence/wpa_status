import socket
import bson
from wpa_status.protocol import Request, Response


class Client():
    def __init__(self, address):
        self._address = address
        self._socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._socket.connect(self._address)

    def request(self, method, params=None):
        request = Request(method, params)
        request_bytes = bson.encode(request.serialize())
        self._socket.sendall(request_bytes)

        response_bytes = self._socket.recv(4096)
        response_bson = bson.decode(response_bytes)
        return Response(response_bson)
