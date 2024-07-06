from src.infra.db.entities.users import Users as UsersEntity
from src.infra.db.interfaces.users_repository import UsersRepositoryInterface


class UsersRepositorySpy(UsersRepositoryInterface):

    @classmethod
    def insert_user(cls, token: str, email: str, username: str, session_id: str) -> None:
        insert_user_attributes = {"token": token,
                                  "email": email,
                                  "username": username,
                                  "session_id": session_id}

    @classmethod
    def select_email(cls, email: str) -> UsersEntity:
        select_user_attributes = {UsersEntity(token="39721cd4-6f50-46c5-9d2a-10f9159b09ee",
                                              username='Lua',
                                              email='lua2@outlook.com',
                                              session_id="session_badlands321301231231231")}
        for user in select_user_attributes:
            if user.email == email:
                return user
            return None

    @classmethod
    def select_username(cls, username: str) -> UsersEntity:
        select_user_attributes = {UsersEntity(token="39721cd4-6f50-46c5-9d2a-10f9159b09ee",
                                              username='Lua',
                                              email='lua2@outlook.com',
                                              session_id="session_badlands321301231231231")}
        for user in select_user_attributes:
            if user.username == username: return user
        return None

    @classmethod
    def remove_user(cls, token: str) -> None:
        return None
