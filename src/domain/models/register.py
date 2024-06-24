#pylint: disable=trailing-comma-tuple
import json

class Register:
    def __init__(self, email: str, username: str, password: str):
        self.email = email
        self.username = username
        self.password = password
    
    def to_dict(self):
        return {
            "email": self.email,
            "username": self.username,
            "password": self.password
        }

    def to_json(self):
        return json.dumps(self.to_dict())