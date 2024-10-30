from src.main.logs.logs_interface import LogInterface


class LogSpy(LogInterface):

    def log_error(self, error: any, message: str): pass

    def log_warning(self, error: any, message: str): pass

    def log_critical(self, error: any, message: str): pass

    def log_session(self, session: any, action: str): pass
