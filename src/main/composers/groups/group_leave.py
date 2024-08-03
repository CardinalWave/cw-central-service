from src.data.use_cases.groups.group_leave import GroupLeave
from src.infra.db.repositories.group.groups_repository import GroupsRepository
from src.main.composers.relations.user_group_composer import user_group_composer
from src.main.composers.relations.validate import validate_composer
from src.presentation.controllers.groups.group_leave_controller import GroupLeaveController
from src.main.logs.logs import Log


def group_leave_composer():

    repository = GroupsRepository()
    validate = validate_composer()
    user_group = user_group_composer()
    logger = Log()
    use_case = GroupLeave(validate=validate,
                          users_groups=user_group,
                          group_repository=repository,
                          logger=logger)
    controller = GroupLeaveController(use_case)

    return controller.handle
