from src.domain.models.group import Group
from src.domain.models.user import User
from src.domain.use_cases.relations.validate import Validate as ValidateInterface
from src.infra.db.interfaces.users_repository import UsersRepositoryInterface
from src.infra.db.interfaces.groups_repository import GroupsRepositoryInterface
from src.data.erros.domain_errors import BadRequestError


class Validate(ValidateInterface):

    def __init__(self, user_repository: UsersRepositoryInterface, group_repository: GroupsRepositoryInterface):
        self.__user_repository = user_repository
        self.__group_repository = group_repository

    def user_email(self, email: str) -> User:
        try:
            user_entity = self.__user_repository.select_email(email)
            user = User(token=user_entity.token, username=user_entity.username, email=user_entity.email)
            return user
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e

    def user_token(self, token: str) -> User:
        try:
            user_entity = self.__user_repository.select_token(token)
            user = User(token=user_entity.token, username=user_entity.username, email=user_entity.email)
            return user
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e

    def group_id(self, group_id: str) -> Group:
        try:
            group_entity = self.__group_repository.select_group_id(group_id=group_id)
            group = Group(group_id=group_entity.id, title=group_entity.title)
            return group
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e

    def group_title(self, group_title: str) -> Group:
        try:
            group_entity = self.__group_repository.select_title(group_title)
            group = Group(group_id=group_entity.id, title=group_entity.title)
            return group
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
