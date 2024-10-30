from abc import ABC, abstractmethod


class GroupLeave(ABC):

    @abstractmethod
    def leave(self, token: str, group_id: str): pass
