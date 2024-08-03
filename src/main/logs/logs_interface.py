from abc import ABC, abstractmethod


class LogInterface(ABC):

    @abstractmethod
    def log_session(self, session: any, action: str): pass

    @abstractmethod
    def log_error(self, error: any, message: str): pass

    @abstractmethod
    def log_warning(self, error: any, message: str): pass

    @abstractmethod
    def log_critical(self, error: any, message: str): pass
