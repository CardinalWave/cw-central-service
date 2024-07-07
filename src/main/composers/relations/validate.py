from src.infra.security.implementations.secure_email import SecureEmail
from src.infra.db.repositories.group.groups_repository import GroupsRepository
from src.infra.db.repositories.users.users_repository import UsersRepository
from src.data.use_cases.relations.validate import Validate


def validate_composer():
    users_rp = UsersRepository()
    groups_rp = GroupsRepository()
    use_case = Validate(users_rp, groups_rp)

    return use_case
