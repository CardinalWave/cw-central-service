from src.presentation.controllers.groups.group_create_controller import GroupCreateController
from src.data.use_cases.groups.group_create import GroupCreate

def group_create_composer():

    use_case = GroupCreate()
    controller = GroupCreateController(use_case)

    return controller.handle
