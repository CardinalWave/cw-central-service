from src.presentation.controllers.groups.group_create_controller import GroupCreateController
from src.data.use_cases.groups.group_create import GroupCreate
from src.infra.db.repositories.group.groups_repository import GroupsRepository


def group_create_composer():
    repository = GroupsRepository()
    use_case = GroupCreate(repository)
    controller = GroupCreateController(use_case)

    return controller.handle
