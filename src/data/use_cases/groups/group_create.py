import uuid
from typing import Dict
from src.domain.models.group import Group
from src.domain.use_cases.groups.group_create import GroupCreate as GroupCreateInterface
from src.infra.db.interfaces.groups_repository import GroupsRepositoryInterface
from src.data.erros.domain_errors import BadRequestError, InternalServerError
from src.domain.models.group import Group


class GroupCreate(GroupCreateInterface):
    def __init__(self, group_repository: GroupsRepositoryInterface):
        self.__group_repository = group_repository

    def create(self, group: Group) -> Dict:
        try:
            self.__validate_name(group.title)
            self.__search_group(group.title)
            group = self.__save_group(group.title)
            return group.to_dict()
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e

    @staticmethod
    def __validate_name(title: str):
        if len(title) < 5 or len(title) > 20:
            raise BadRequestError('Titulo invalido')
        if "global" in title.lower():
            raise BadRequestError('Titulo invalido')

    def __search_group(self, title: str):
        group = self.__group_repository.select_title(title=title)
        if group:
            raise BadRequestError('Grupo ja existente')

    def __save_group(self, title: str) -> Group:
        group_id = str(uuid.uuid4())
        self.__group_repository.add_group(id=group_id, title=title)
        return Group(group_id=group_id, title=title)
