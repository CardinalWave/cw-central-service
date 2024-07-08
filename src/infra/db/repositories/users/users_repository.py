from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from src.infra.db.interfaces.users_repository import UsersRepositoryInterface
from src.data.erros.domain_errors import InternalServerError


class UsersRepository(UsersRepositoryInterface):

    @classmethod
    def insert_user(cls, token: str, email: str, username: str, device: str, session_id: str) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = UsersEntity(
                    token=token,
                    email=email,
                    username=username,
                    device=device,
                    session_id=session_id
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
    def select_session(cls, session_id: str) -> UsersEntity:
        with DBConnectionHandler() as database:
            try:
                user = (
                    database.session
                    .query(UsersEntity)
                    .filter(UsersEntity.session_id == session_id)
                    .first()
                )
                return user
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

    @classmethod
    def select_device(cls, device: str) -> list[UsersEntity]:
        with DBConnectionHandler() as database:
            try:
                user_list = (
                    database.session
                    .query(UsersEntity)
                    .filter(UsersEntity.device == device)
                    .all()
                )
                return user_list
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

    @classmethod
    def select_token(cls, token: str) -> UsersEntity:
        with DBConnectionHandler() as database:
            try:
                user = (
                    database.session
                    .query(UsersEntity)
                    .filter(UsersEntity.token == token)
                    .first()
                )

                return user
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

    @classmethod
    def remove_user(cls, token: str) -> str:
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
                    return "success"
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e
            return "error"
