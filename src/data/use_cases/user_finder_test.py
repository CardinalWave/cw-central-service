from typing import List
from src.domain.models.users import Users
from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_finder import UserFinder

def test_find():
    first_name = 'name'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)
    assert repo.select_user_attributes["first_name"]  == first_name

    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []

def test_find_error_in_valid_name():
    first_name = 'name_ok'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome invalido para a busca"

def test_find_error_in_long_name():
    first_name = 'nameokNomeinvalidoparaabusca'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "Nome muito grande para a busca"

def test_find_error_user_not_found():
    class UserRepositoryError(UsersRepositorySpy):
        def select_user(self, first_name: str) -> List[Users]:
            return []

    first_name = 'name'

    repo = UserRepositoryError()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as exception:
        assert str(exception) == "Usuario nao encontrado"
