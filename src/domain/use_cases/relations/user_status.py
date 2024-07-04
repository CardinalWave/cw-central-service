from abc import ABC, abstractmethod
from src.domain.enums.UserStatusType import UserStatusType
from src.domain.models.group import Group


class UserStatus(ABC):
    @abstractmethod
    def receiver_status(self, secure_email) -> UserStatusType: pass

    @abstractmethod
    def update_status(self, secure_email): pass

    @abstractmethod
    def in_group(self, secure_email, group: Group) -> UserStatusType: pass
