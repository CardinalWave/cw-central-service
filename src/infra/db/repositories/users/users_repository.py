from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from src.infra.db.interfaces.users_repository import UsersRepositoryInterface
from src.data.erros.domain_errors import InternalServerError

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
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

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
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

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
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

    @classmethod
    def remove_user(cls, token: str) ->  UsersEntity:
        with DBConnectionHandler() as database:
            try:
                user = (
                    database.session
                        .query(UsersEntity)
                        .filter(UsersEntity.token == token)
                        .first()
                )
                if user:
                    database.session.delete(user)
                    database.session.commit()
                return user
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e
