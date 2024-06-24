#pylint: disable=trailing-comma-tuple
import json

class Login:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "email": self.email,
            "password": self.password
        }

    def to_json(self):
        return json.dumps(self.to_dict())
