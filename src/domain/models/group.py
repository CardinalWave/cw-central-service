#pylint: disable=trailing-comma-tuple
import json


class Group:
    def __init__(self, group_id: str, title: str):
        self.group_id = group_id
        self.title = title

    def to_dict(self):
        return {
            "group_id": self.group_id,
            "title": self.title
        }

    def to_json(self):
        return json.dumps(self.to_dict())
