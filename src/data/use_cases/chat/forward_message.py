#pylint: disable=too-many-arguments
import http.client
from src.domain.use_cases.chat.forward_message import ForwardMessage as ForwardMessageInterface
from src.data.erros.domain_errors import BadRequestError
from src.main.logs.logs import Log
from src.config.config import Config


class ForwardMessage(ForwardMessageInterface):

    def __init__(self):
        self.msg_service_ip = Config.CW_MESSAGE_SERVICE_IP
        self.msg_service_port = Config.CW_MESSAGE_SERVICE_PORT
        self.__logger = Log()

    def send_message(self, params: any, action: str):
        self.__request_message(params=params, action=action)

    def __request_message(self, params: any, action):
        try:
            self.__logger.log_session(session=params, action=f'request - {action}')
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
            self.__logger.log_warning(error=e,
                                      message=f'Falha na requisicao [Parametros = {params},'
                                              f'URL = '
                                              f'http://{self.msg_service_ip}:'
                                              f'{self.msg_service_port}{action}]')

            raise BadRequestError(e) from e
