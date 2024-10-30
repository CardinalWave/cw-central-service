#pylint: disable=too-many-arguments
from abc import ABC, abstractmethod


class ForwardMessage(ABC):

    @abstractmethod
    def send_message(self, params: any, action: str): pass
