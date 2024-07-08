#pylint: disable=too-many-arguments
import datetime
import http.client
from typing import Dict
from src.domain.models.group import Group
from src.domain.models.user import User
from src.domain.models.message import Message
from src.domain.models.session import Session
from src.domain.use_cases.chat.forward_message import ForwardMessage as ForwardMessageInterface
from src.data.erros.domain_errors import BadRequestError


class ForwardMessage(ForwardMessageInterface):
    cw_message_service = ""

    @classmethod
    def send_message(cls, user: User, group: Group, session: Session, message: Dict, action: str):
        updated_at = datetime.datetime.now()
        payload = cls.__format_message(user=user,
                                       group=group,
                                       session=session,
                                       send_time=updated_at,
                                       action=action,
                                       message=message)
        cls.__request_message(payload, cls.cw_message_service, action)

    @staticmethod
    def __format_message(user: User,
                         group: Group,
                         session: Session,
                         send_time: datetime,
                         action: str, message: Dict):
        try:
            message = Message(group_id=group.group_id,
                              username=user.username,
                              session=session,
                              send_time=send_time,
                              action=action,
                              payload=message)
            return message
        except Exception as e:
            raise BadRequestError(e) from e

    @staticmethod
    def __request_message(params: any, url: str, action):
        try:
            headers = {
                'Content-type': 'application/json'
            }

            conn = http.client.HTTPSConnection(url)
            conn.sock.settimeout(10)
            route = '/chat/' + action
            conn.request("POST", route, params, headers)
            response = conn.getresponse()
            if response.status != 200:
                raise ValueError("Request error")

            # data = response.read()
            # json_data = json.loads(data)
            conn.close()
        except Exception as e:
            raise BadRequestError(e) from e
