from src.infra.db.repositories.relations.users_groups_repository import UsersGroupsRepository
from src.infra.security.implementations.secure_email import SecureEmail
from src.data.use_cases.relations.user_group import UserGroup


def user_group_composer():
    secure_email = SecureEmail()
    repository = UsersGroupsRepository()
    use_case = UserGroup(repository, secure_email)

    return use_case
