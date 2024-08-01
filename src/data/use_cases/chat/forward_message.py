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
from src.main.logs.logs import log_session, log_warning


class ForwardMessage(ForwardMessageInterface):

    def __init__(self):
        self.cw_message_service_ip = "192.168.15.69"
        self.cw_message_service_port = 5001

    def send_message(self, params: any, action: str):
        self.__request_message(params=params, action=action)

    def __request_message(self, params: any, action):
        try:
            log_session(session=params, action=f'request - {action}')
            headers = {
                'Content-type': 'application/json'
            }
            conn = http.client.HTTPConnection(host='192.168.15.69', port=5001)
            conn.request("POST", action, params, headers)
            conn.sock.settimeout(10)
            response = conn.getresponse()
            if response.status != 200:
                raise ValueError("Request error")
            conn.close()
        except Exception as e:
            log_warning(error=e, message=f'Falha na requisicao [Parametros = {params},'
                                         f'URL = http://{self.cw_message_service_ip}:{self.cw_message_service_port}{action}]')
            raise BadRequestError(e) from e
