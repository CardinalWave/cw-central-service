#pylint: disable=trailing-comma-tuple
#pylint: disable=too-many-arguments
import json
import datetime
from src.domain.models.session import Session


class Message:
    def __init__(self, group_id: str,
                 username: str,
                 session: Session,
                 send_time: datetime,
                 action: str,
                 payload):

        self.group_id = group_id
        self.username = username
        self.session = session
        self.send_time = send_time
        self.action = action
        self.payload = payload

    def to_dict(self):
        return {
            "group_id": self.group_id,
            "username": self.username,
            "session": self.session.to_dict(),
            "send_time": self.send_time,
            "action": self.action,
            "payload": self.payload
        }

    def to_json(self):
        return json.dumps(self.to_dict())
