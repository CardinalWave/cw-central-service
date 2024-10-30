from src.data.use_cases.groups.group_list import GroupList
from src.presentation.controllers.groups.group_list_controller import GroupListController
from src.main.composers.relations.user_group_composer import user_group_composer
from src.main.composers.relations.validate import validate_composer
from src.main.composers.groups.group_join_composer import group_join_composer
from src.data.use_cases.groups.group_join import GroupJoin
from src.infra.db.repositories.group.groups_repository import GroupsRepository




def group_list_composer():
    validate = validate_composer()
    user_group = user_group_composer()
    group_repository = GroupsRepository()
    group_join = GroupJoin(users_groups=user_group, group_repository=group_repository, validate=validate)
    use_case = GroupList(user_group, validate, group_join)
    controller = GroupListController(use_case)

    return controller.handle
