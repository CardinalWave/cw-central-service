import datetime
from src.main.logs.logs_interface import LogInterface
from src.main.logs.log_handler import logger


class Log(LogInterface):

    def __init__(self):
        self.service = "cw-central-service"
        self.ip = "192.168.15.69"
        self.port = "0000"
        self.local_service = f'{self.service}:{self.ip}:{self.port}'

    def log_session(self, session: any, action: str):
        log_payload = {
            'time': datetime.datetime.now(),
            'service': self.local_service,
            'action': action,
            'payload': str(session)
        }
        logger.info(log_payload)

    def log_error(self, error: any, message: str):
        log_payload = {
            'time': datetime.datetime.now(),
            'service': self.local_service,
            'error': str(error),
            'message': message
        }
        logger.error(log_payload)

    def log_warning(self, error: any, message: str):
        log_payload = {
            'time': datetime.datetime.now(),
            'service': self.local_service,
            'error': str(error),
            'message': message
        }
        logger.warning(log_payload)

    def log_critical(self, error: any, message: str):
        log_payload = {
            'time': datetime.datetime.now(),
            'service': self.local_service,
            'error': str(error),
            'message': message
        }
        logger.critical(log_payload)
