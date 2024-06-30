from src.infra.db.entities.groups import Groups as GroupsEntity
from src.infra.db.interfaces.groups_repository import GroupsRepositoryInterface

class GroupsRepositorySpy(GroupsRepositoryInterface):

    def add_group(self, id: str, title: str) -> GroupsEntity:
        return GroupsEntity(id=id, title=title)
    
    def select_title(self, title: str) -> GroupsEntity:
        groupsEntity = GroupsEntity(id="dalsj-dlad-dasad", title="TestGroup")
        if groupsEntity.title == title:
            return groupsEntity
        return None
