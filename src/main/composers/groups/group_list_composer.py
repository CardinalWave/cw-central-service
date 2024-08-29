from src.data.use_cases.groups.group_list import GroupList
from src.presentation.controllers.groups.group_list_controller import GroupListController
from src.main.composers.relations.user_group_composer import user_group_composer
from src.main.composers.relations.validate import validate_composer


def group_list_composer():
    validate = validate_composer()
    user_group = user_group_composer()
    use_case = GroupList(user_group, validate)
    controller = GroupListController(use_case)

    return controller.handle
