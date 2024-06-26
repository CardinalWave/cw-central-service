from typing import Dict
from src.domain.models.user import User
from src.domain.models.register import Register
from src.domain.use_cases.users.user_resgister import UserRegister as UserRegisterInterface


class UserRegisterSpy(UserRegisterInterface):

    @classmethod
    def register(cls, register: Register) -> Dict:
        return User(token="39721cd4-6f50-46c5-9d2a-10f9159b09ee",
                    email=register.email,
                    username=register.email).to_dict()
