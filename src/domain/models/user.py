#pylint: disable=redefined-builtin
import json

class User:
    def __init__(self, token: str, email: str, username: str) -> None:
        self.token = token
        self.email = email
        self.username = username

    def to_dict(self):
        return {
            "token": self.token,
            "email": self.email,
            "username": self.username
        }

    def to_json(self):
        return json.dumps(self.to_dict())