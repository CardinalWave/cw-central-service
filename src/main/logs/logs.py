import datetime
from src.main.logs.log_handler import logger

SERVICE = "cw-central-service"
IP = "192.168.15.69"
PORT = "0000"

LOCAL_SERVICE = f'{SERVICE}:{IP}:{PORT}'


def log_session(session: any, action: str):
    log_payload = {
        'time': datetime.datetime.now(),
        'service': LOCAL_SERVICE,
        'action': action,
        'payload': str(session)
    }
    logger.info(log_payload)


def log_error(error: any, message: str):
    log_payload = {
        'time': datetime.datetime.now(),
        'service': LOCAL_SERVICE,
        'error': str(error),
        'message': message
    }
    logger.error(log_payload)


def log_warning(error: any, message: str):
    log_payload = {
        'time': datetime.datetime.now(),
        'service': LOCAL_SERVICE,
        'error': str(error),
        'message': message
    }
    logger.warning(log_payload)


def log_critical(error: any, message: str):
    log_payload = {
        'time': datetime.datetime.now(),
        'service': LOCAL_SERVICE,
        'error': str(error),
        'message': message
    }
    logger.critical(log_payload)
