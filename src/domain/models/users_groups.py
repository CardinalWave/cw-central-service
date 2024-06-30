#pylint: disable=redefined-builtin
import json

class UsersGroups:
    def __init__(self, id: str, secure_email: str, group_title: str, group_id: str, updated_at: str) -> None:
        self.id = id
        self.secure_email = secure_email
        self.group_title = group_title
        self.group_id = group_id
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id,
            "secure_email": self.secure_email,
            "group_title": self.group_title,
            "group_id": self.group_id,
            "updated_at": self.updated_at
        }

    def to_json(self):
        return json.dumps(self.to_dict())
