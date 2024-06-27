#pylint: disable=trailing-comma-tuple
import json

class Group:
    def __init__(self, id: str, title: str):
        self.id = id
        self.title = title

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title
        }

    def to_json(self):
        return json.dumps(self.to_dict())
