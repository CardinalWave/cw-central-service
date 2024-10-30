#pylint: disable=redefined-builtin
import json


class Session:
    def __init__(self, session_id: str, device: str) -> None:
        self.session_id = session_id
        self.device = device

    def to_dict(self):
        return {
            "session_id": self.session_id,
            "device": self.device
        }

    def to_json(self):
        return json.dumps(self.to_dict())
