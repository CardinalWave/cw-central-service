from src.data.use_cases.groups.group_list import GroupList
from src.presentation.controllers.groups.group_list_controller import GroupListController
from src.main.composers.relations.user_group_composer import user_group_composer

def group_list_composer():

    user_group = user_group_composer()
    use_case = GroupList(user_group)
    controller = GroupListController(use_case)

    return controller.handle
