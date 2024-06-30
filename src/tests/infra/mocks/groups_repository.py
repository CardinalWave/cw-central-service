#pylint: disable=redefined-outer-name, redefined-builtin
from src.infra.db.entities.groups import Groups as GroupsEntity
from src.infra.db.interfaces.groups_repository import GroupsRepositoryInterface

class GroupsRepositorySpy(GroupsRepositoryInterface):

    @classmethod
    def add_group(cls, id: str, title: str) -> GroupsEntity:
        return GroupsEntity(id=id, title=title)

    @classmethod
    def select_title(cls, title: str) -> GroupsEntity:
        groups_entity = GroupsEntity(id="dalsj-dlad-dasad", title="TestGroup")
        if groups_entity.title == title:
            return groups_entity
        return None
