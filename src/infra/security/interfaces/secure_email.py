from abc import ABC, abstractmethod
from cryptography.fernet import Fernet


class SecureEmailInterface(ABC):

    @abstractmethod
    def encrypt_email(self, email: str) -> str: pass
