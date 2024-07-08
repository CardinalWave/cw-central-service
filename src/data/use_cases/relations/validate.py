from src.domain.models.group import Group
from src.domain.models.user import User
from src.domain.models.session import Session
from src.domain.use_cases.relations.validate import Validate as ValidateInterface
from src.infra.db.interfaces.users_repository import UsersRepositoryInterface
from src.infra.db.interfaces.users_groups_repository import UsersGroupsRepositoryInterface
from src.data.erros.domain_errors import BadRequestError


class Validate(ValidateInterface):

    def __init__(self, user_repository: UsersRepositoryInterface,
                 users_group_repository: UsersGroupsRepositoryInterface):
        self.__user_repository = user_repository
        self.__users_group_repository = users_group_repository

    def user_email(self, email: str) -> User:
        try:
            user_entity = self.__user_repository.select_email(email)
            user = User(token=user_entity.token,
                        username=user_entity.username,
                        email=user_entity.email)
            return user
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e

    def user_token(self, token: str) -> User:
        try:
            user_entity = self.__user_repository.select_token(token)
            user = User(token=user_entity.token,
                        username=user_entity.username,
                        email=user_entity.email)
            return user
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e

    def user_session_token(self, token: str) -> tuple:
        try:
            user_entity = self.__user_repository.select_token(token)
            user = User(token=user_entity.token,
                        username=user_entity.username,
                        email=user_entity.email)

            session = Session(session_id=user_entity.session_id,
                              device=user_entity.device)
            return user, session
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e

    def group_id(self, group_id: str, email: str) -> Group:
        try:
            users_group_entitys = self.__users_group_repository.select_user_relations(email)
            for entity in users_group_entitys:
                if entity.group_id == group_id:
                    group = Group(group_id=entity.group_id, title=entity.group_title)
                    return group
            return None
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e

    def group_title(self, group_title: str, email: str) -> Group:
        try:
            users_group_entitys = self.__users_group_repository.select_user_relations(email)
            for entity in users_group_entitys:
                if entity.group_title == group_title:
                    return Group(group_id=entity.group_id, title=entity.group_title)
            return None
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
