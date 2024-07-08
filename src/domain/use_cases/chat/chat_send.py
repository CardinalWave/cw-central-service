from abc import ABC
from typing import Dict


class ChatSend(ABC):

    def send(self, token: str, group_id: str, message: str) -> Dict: pass
