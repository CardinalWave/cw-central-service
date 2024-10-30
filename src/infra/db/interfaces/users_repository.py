from abc import ABC, abstractmethod
from src.infra.db.entities.users import Users as UsersEntity
from src.domain.models.session import Session


class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, token: str, email: str, username: str, device: str, session_id: str) -> None: pass

    @abstractmethod
    def select_email(self, email: str) -> UsersEntity: pass

    @abstractmethod
    def select_session(self, session_id: str) -> UsersEntity: pass

    @abstractmethod
    def select_username(self, username: str) -> UsersEntity: pass

    @abstractmethod
    def select_device(self, device: str) -> list[UsersEntity]: pass

    @abstractmethod
    def select_token(self, token: str) -> UsersEntity: pass

    @abstractmethod
    def remove_user(self, token: str) -> str: pass
