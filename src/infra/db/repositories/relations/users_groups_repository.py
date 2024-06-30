import datetime
from typing import List
from src.domain.models.users_groups import UsersGroups
from src.infra.db.entities.groups import Groups as GroupsEntity
from src.infra.db.entities.users import Users as UsersEntity
from src.infra.db.entities.users_groups import UsersGroups as UsersGroupsEntity
from src.infra.db.interfaces.users_groups_repository import UsersGroupsRepositoryInterface
from src.infra.db.settings.connection import DBConnectionHandler
from src.data.erros.domain_errors import InternalServerError

class UsersGroupsRepository(UsersGroupsRepositoryInterface):

    @classmethod
    def join_user(self, id: str, secure_email, group_title: str, group_id: str, updated_at: datetime) -> UsersGroupsEntity:
        with DBConnectionHandler() as database:
            try:
                new_registry = UsersGroupsEntity(
                    id=id,
                    secure_email=secure_email,
                    group_title=group_title,
                    group_id=group_id,
                    updated_at=updated_at
                )
                database.session.add(new_registry)
                database.session.commit()
                return new_registry
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

    # Grupos do Usuario
    @classmethod
    def select_user_relations(self, secure_email: str) -> List[UsersGroupsEntity]:
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

    # Usuarios no Grupo
    @classmethod
    def select_group_relations(self, group_id: str) -> List[UsersGroupsEntity]:
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
    def update_relation(self, secure_email: str, group_id: str, updated_at: datetime) -> UsersGroupsEntity:
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
