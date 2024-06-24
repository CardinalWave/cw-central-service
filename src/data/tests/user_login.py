from typing import Dict
from src.domain.use_cases.user_login import UserLogin as UserLoginInterface
from src.domain.models.login import Login
from src.domain.models.user import User

class UserLoginSpy(UserLoginInterface):

    @classmethod
    def login(self, login: Login) -> Dict:
        user = User(token="39721cd4-6f50-46c5-9d2a-10f9159b09ee", email=login.email, username="Lua")
        return user.to_json()
