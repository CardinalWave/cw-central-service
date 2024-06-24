from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from src.data.interfaces.users_repository import UsersRepositoryInterface

class UsersRepository(UsersRepositoryInterface):

    @classmethod
    def insert_user(cls, token: str, email: str, username: str) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = UsersEntity(
                    token=token,
                    email=email,
                    username=username
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_email(cls, email: str) -> UsersEntity:
        with DBConnectionHandler() as database:
            try:
                user = (
                    database.session
                        .query(UsersEntity)
                        .filter(UsersEntity.email == email)
                        .first()
                )
                return user
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_username(cls, username: str) -> UsersEntity:
        with DBConnectionHandler() as database:
            try:
                user = (
                    database.session
                        .query(UsersEntity)
                        .filter(UsersEntity.username == username)
                        .first()
                )
                return user
            except Exception as exception:
                database.session.rollback()
                raise exception
