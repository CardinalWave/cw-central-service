#pylint: disable=redefined-builtin
from src.infra.db.interfaces.groups_repository import GroupsRepositoryInterface
from src.infra.db.entities.groups import Groups as GroupsEntity
from src.infra.db.settings.connection import DBConnectionHandler
from src.data.erros.domain_errors import InternalServerError

class GroupsRepository(GroupsRepositoryInterface):

    @classmethod
    def add_group(cls, id: str, title: str) -> GroupsEntity:
        with DBConnectionHandler() as database:
            group_entity = GroupsEntity(
                    id=id,
                    title=title
                )
            try:
                new_registry = group_entity
                database.session.add(new_registry)
                database.session.commit()
                return group_entity
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

    @classmethod
    def select_title(cls, title: str) -> GroupsEntity:
        with DBConnectionHandler() as database:
            try:
                group_entity = (
                    database.session
                        .query(GroupsEntity)
                        .filter(GroupsEntity.title == title)
                        .first()
                )
                return group_entity
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e

    @classmethod
    def select_group_id(cls, group_id: str) -> GroupsEntity:
        with DBConnectionHandler() as database:
            try:
                group = (
                    database.session
                    .query(GroupsEntity)
                    .filter(GroupsEntity.id == group_id)
                    .first()
                )
                return group
            except Exception as e:
                database.session.rollback()
                raise InternalServerError(str(e)) from e
