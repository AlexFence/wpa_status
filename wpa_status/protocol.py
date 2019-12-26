import uuid
from abc import ABC, abstractmethod
from enum import Enum


class Method(Enum):
    PING = "PING"
    STATUS = "STATUS"
    LIST_NETWORKS = "LIST_NETWORKS"
    SUPPLICANT_RUNNING = "SUPPLICANT_RUNNING"


class Message(ABC):
    def __init__(self, dict):
        self._type = dict["type"]
        self._id = dict["id"]

        method = dict["method"]
        if method.__class__ is not Method:
            method = Method(method)

        self._method = method

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @property
    def method(self):
        return self._method

    @abstractmethod
    def serialize(self):
        return {"id": self.id, "type": self.type, "method": self.method.value}


class Response(Message):
    def __init__(self, dict):
        super().__init__(dict)
        self._result = dict["result"]

    @property
    def result(self):
        return self._result

    def serialize(self):
        base = super().serialize()
        base["result"] = self.result
        return base


class Request(Message):
    def __init__(self, method, params=None):
        id = str(uuid.uuid4())
        super().__init__({"id":  id, "method": method, "type": "Request"})
        self._params = params

    @property
    def params(self):
        return self._params

    def serialize(self):
        base = super().serialize()
        base["params"] = self.params
        return base
