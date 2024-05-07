from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_register import UserRegister

def test_register():
    first_name = "ola"
    last_name = "aqui"
    age = 3

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    response = user_register.register(first_name, last_name, age)

    assert repo.insert_user_attributes["first_name"] == first_name

    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributes"]

def test_register_first_name_error():
    first_name = "ola 123 _"
    last_name = "ok"
    age = 3

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)


    try:
        user_register.register(first_name, last_name, age)
    except Exception as exception:
        assert str(exception) == "Nome invalido para o registro"
