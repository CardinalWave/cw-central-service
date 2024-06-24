from src.domain.models.user import User

class UsersRepositorySpy():

    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {User(token="39721cd4-6f50-46c5-9d2a-10f9159b09ee",
                                            username='Lua',
                                            email='lua2@outlook.com')}

    def insert_user(self, token: str, email: str, username: int) -> None:
        self.insert_user_attributes["token"] = token
        self.insert_user_attributes["email"] = email
        self.insert_user_attributes["username"] = username

    def select_user(self, email: str) -> User:
        for user in self.select_user_attributes:
            if user.email == email:return user
        return None
