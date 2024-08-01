import json
from src.domain.use_cases.groups.group_leave import GroupLeave as GroupLeaveInterface
from src.infra.db.interfaces.groups_repository import GroupsRepositoryInterface
from src.domain.use_cases.relations.user_group import UserGroup as UserGroupInterface
from src.domain.use_cases.relations.validate import Validate as ValidateInterface
from src.domain.models.group import Group
from src.data.erros.domain_errors import BadRequestError, InternalServerError
from src.main.logs.logs import log_session, log_error


class GroupLeave(GroupLeaveInterface):

    def __init__(self,
                 group_repository: GroupsRepositoryInterface,
                 users_groups: UserGroupInterface,
                 validate: ValidateInterface):
        self.__group_repository = group_repository
        self.__users_groups = users_groups
        self.__validate = validate

    def leave(self, token: str, group_id: str):
        try:
            log_session(action="group_leave", session=[token, group_id])
            user = self.__validate.user_token(token)
            found_group = self.__search_group(group_id)
            self.__search_member(email=user.email, title=found_group.title)
            self.__remove_user(user.token, found_group.group_id)
        except BadRequestError as e:
            log_error(error=e, message=str(e))
            raise BadRequestError(str(e)) from e
        except Exception as e:
            log_error(error=e, message=str(e))
            raise InternalServerError(str(e)) from e

    def __remove_user(self, token: str, group_id: str):
        try:
            self.__users_groups.remove_user(user_token=token, group_id=group_id)
        except BadRequestError as e:
            log_error(error=e, message=str(e))
            raise BadRequestError(str(e)) from e
        except Exception as e:
            log_error(error=e, message=str(e))
            raise InternalServerError(str(e)) from e

    def __search_group(self, group_id: str) -> Group:
        group_repo = self.__group_repository.select_group_id(group_id=group_id)
        group = Group(group_id=group_repo.id, title=group_repo.title)
        if group.title != 'GLOBAL':
            return group

    def __search_member(self, email: str, title: str) -> None:
        groups = self.__users_groups.select_user_relations(email=email)

        group_found = False

        for group in groups:
            if group.title == title:
                group_found = True
                break

        if not group_found:
            log_error(error=BadRequestError, message="Nenhum grupo com o título fornecido encontrado")
            raise BadRequestError("Nenhum grupo com o título fornecido encontrado")