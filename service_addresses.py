from abc import ABC, abstractmethod
from enum import Enum


class MicroService(ABC):
    def __init__(self, full_address, port):
        self._full_address = full_address
        self._port = port

    @property
    def full_address(self):
        return self._full_address

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        self._port = value

    @abstractmethod
    def get_POST_endpoint(self):
        pass

    @abstractmethod
    def get_GET_endpoint(self):
        pass


class FacadeService(MicroService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.POST_suffix = "/message"
        self.GET_suffix = "/messages"

    def get_POST_endpoint(self):
        return self.full_address + self.POST_suffix

    def get_GET_endpoint(self):
        return self.full_address + self.GET_suffix


class LoggingService(MicroService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.POST_suffix = "/log"
        self.GET_suffix = "/logs"

    def get_POST_endpoint(self):
        return self.full_address + self.POST_suffix

    def get_GET_endpoint(self):
        return self.full_address + self.GET_suffix


class StaticService(MicroService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.GET_suffix = "/message"

    def get_GET_endpoint(self):
        return self.full_address + self.GET_suffix

    def get_POST_endpoint(self):
        raise NotImplementedError("Static service does not support POST requests")


FACADE_SERVICE = FacadeService("http://localhost:5000", 5000)
LOGGING_SERVICE = LoggingService("http://localhost:5001", 5001)
STATIC_SERVICE = StaticService("http://localhost:5002", 5002)


class MicroServiceAddresses(Enum):
    FACADE = FACADE_SERVICE
    LOGGING = LOGGING_SERVICE
    STATIC = STATIC_SERVICE
