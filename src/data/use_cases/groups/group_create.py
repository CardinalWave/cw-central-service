import uuid
from typing import Dict
from src.domain.models.group import Group
from src.domain.use_cases.groups.group_create import GroupCreate as GroupCreateInterface
from src.infra.db.interfaces.groups_repository import GroupsRepositoryInterface
from src.data.erros.domain_errors import BadRequestError, InternalServerError
from src.domain.models.group import Group

class GroupCreate(GroupCreateInterface):
    def __init__(self, group_repository: GroupsRepositoryInterface) -> Group:
        self.__group_repository = group_repository

    def create(self, title: str) -> None:
        try:
            self.__validate_name(title) 
            self.__search_group(title)
            group = self.__save_group(title)
            return group
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e

    def __validate_name(title: str) -> None:
        if len(title) < 5 | len(title) > 20:
            raise BadRequestError('Titulo invalido invalido')
        if "global" in title.lower():
            raise BadRequestError('Titulo invalido invalido') 

    def __search_group(self, title: str) -> None:
        users = self.__group_repository.select_title(title=title)
        if users:
            raise BadRequestError('Titulo invalido invalido')

    def __save_group(self, title: str) -> None:
        group_id = uuid.uuid4()
        self.__group_repository.add_group(id=group_id, title=title)
        return Group(id=group_id, title=title)
