import socket
import bson
from wpa_status.protocol import Request, Response, Error


class Client():
    def __init__(self, address):
        self._address = address
        self._create_socket()

    def _create_socket(self):
        self._socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._socket.connect(self._address)

    def request(self, method, params=None):
        # TODO figure out why it throws a BrokenPipeError on reuse
        try:
            request = Request(method, params)
            request_bytes = bson.encode(request.serialize())
            self._socket.sendall(request_bytes)

            response_bytes = self._socket.recv(4096 * 2)
            response_dict = bson.decode(response_bytes)
            if response_dict["type"] == "Response":
                return Response(response_dict)
            else:
                return Error(response_dict)
        except BrokenPipeError:
            self._create_socket()
            return self.request(method, params)
