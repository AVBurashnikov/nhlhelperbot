from abc import ABC, abstractmethod


class Controller(ABC):
    @abstractmethod
    def handler(self, *args, **kwargs):
        pass

    @abstractmethod
    def builder(self, *args, **kwargs):
        pass

    def send_message(self):
        pass
