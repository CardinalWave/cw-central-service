from src.infra.db.repositories.group.groups_repository import GroupsRepository
from src.data.use_cases.groups.group_join import GroupJoin
from src.main.composers.relations.user_group_composer import user_group_composer
from src.presentation.controllers.groups.group_join_controller import GroupJoinController
from src.main.composers.relations.validate import validate_composer


def group_join_composer():
    group_repository = GroupsRepository()
    user_group = user_group_composer()
    validate = validate_composer()
    use_case = GroupJoin(group_repository, user_group, validate)
    controller = GroupJoinController(use_case)

    return controller.handle
