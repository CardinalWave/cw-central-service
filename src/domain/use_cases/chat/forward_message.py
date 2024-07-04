import datetime
from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.group import Group
from src.domain.models.user import User


class ForwardMessage(ABC):

    @abstractmethod
    def join_group(self, user: User, group: Group, updated_at: datetime): pass

    @abstractmethod
    def send_message(self, user: User, group: Group, message: Dict): pass

    @abstractmethod
    def logout_group(self, user: User, group: Group, updated_at: datetime): pass
