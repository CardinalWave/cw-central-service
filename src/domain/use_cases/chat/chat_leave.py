from abc import ABC, abstractmethod


class ChatLeave(ABC):

    @abstractmethod
    def leave(self, token: str): pass
