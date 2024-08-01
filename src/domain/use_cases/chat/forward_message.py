#pylint: disable=too-many-arguments
from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.group import Group
from src.domain.models.user import User
from src.domain.models.session import Session


class ForwardMessage(ABC):

    @abstractmethod
    def send_message(self, params: any, action: str): pass
