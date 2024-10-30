#pylint: disable=redefined-builtin, too-many-arguments
import datetime
from src.infra.db.entities.users_groups import UsersGroups as UsersGroupsEntity
from src.infra.db.interfaces.users_groups_repository import UsersGroupsRepositoryInterface
from src.infra.db.settings.connection import DBConnectionHandler
from src.data.erros.domain_errors import InternalServerError


class UsersGroupsRepository(UsersGroupsRepositoryInterface):

    @classmethod
    def join_user(cls, id: str,
                  secure_email: str,
                  user_token: str,
                  username: str,
                  group_title: str,
                  group_id: str,
                  updated_at: datetime):

        with DBConnectionHandler() as database:
            try:
                new_registry = UsersGroupsEntity(
                    id=id,
                    secure_email=secure_email,
                    user_token=user_token,
                    username=username,
                    group_title=group_title,
                    group_id=group_id,
                    updated_at=updated_at
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

    @classmethod
    def select_user_relations(cls, secure_email: str) -> list[UsersGroupsEntity]:
        with DBConnectionHandler() as database:
            try:
                entitys = (
                    database.session
                    .query(UsersGroupsEntity)
                    .filter(UsersGroupsEntity.secure_email == secure_email)
                    .all()
                )
                return entitys
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

    @classmethod
    def select_group_relations(cls, group_id: str) -> list[UsersGroupsEntity]:
        with DBConnectionHandler() as database:
            try:
                entitys = (
                    database.session
                    .query(UsersGroupsEntity)
                    .filter(UsersGroupsEntity.group_id == group_id)
                    .all()
                )
                return entitys
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

    @classmethod
    def update_relation(cls,
                        secure_email: str,
                        group_id: str,
                        updated_at: datetime) -> UsersGroupsEntity:

        with DBConnectionHandler() as database:
            try:
                (
                    database.session
                    .query(UsersGroupsEntity)
                    .filter(UsersGroupsEntity.secure_email == secure_email)
                    .filter(UsersGroupsEntity.group_id == group_id)
                    .update({"updated_at": updated_at})
                )
                entity = (
                    database.session
                    .query(UsersGroupsEntity)
                    .filter(UsersGroupsEntity.secure_email == secure_email)
                    .filter(UsersGroupsEntity.group_id == group_id)
                    .first()
                )
                return entity
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

    @classmethod
    def remove_user(cls, user_token: str, group_id: str):
        with DBConnectionHandler() as database:
            try:
                entity = (
                    database.session
                    .query(UsersGroupsEntity)
                    .filter(UsersGroupsEntity.user_token == user_token)
                    .filter(UsersGroupsEntity.group_id == group_id)
                    .first()
                )
                database.session.delete(entity)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e
