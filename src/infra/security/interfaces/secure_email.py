from abc import ABC, abstractmethod
from cryptography.fernet import Fernet


class SecureEmail(ABC):

    @abstractmethod
    def encrypt_email(email: str) -> str: pass

    @abstractmethod
    def decrypt_email(self, encrypted_email_b64: str) -> str: pass