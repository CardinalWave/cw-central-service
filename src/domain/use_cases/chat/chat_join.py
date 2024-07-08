from abc import ABC, abstractmethod
from typing import Dict


class ChatJoin(ABC):

    @abstractmethod
    def join(self, group_id: str, token: str) -> Dict: pass
