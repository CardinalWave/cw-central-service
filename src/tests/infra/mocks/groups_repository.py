#pylint: disable=redefined-outer-name, redefined-builtin
from src.infra.db.entities.groups import Groups as GroupsEntity
from src.infra.db.interfaces.groups_repository import GroupsRepositoryInterface

class GroupsRepositorySpy(GroupsRepositoryInterface):

    @classmethod
    def add_group(cls, id: str, title: str) -> GroupsEntity:
        return GroupsEntity(id=id, title=title)

    @classmethod
    def select_title(cls, title: str) -> GroupsEntity:
        groups_entity =  GroupsEntity(id="dalsj-dlad-dasad", title="TestGroup")
        if groups_entity.title == title:
            return groups_entity
        return None

    @classmethod
    def select_group_id(cls, group_id: str) -> GroupsEntity:
        group_entity =  GroupsEntity(id="dalsj-dlad-dasad", title="TestGroup")
        if group_entity.id == group_id:
            return group_entity
        return None
