from abc import ABC, abstractmethod

class SecureEmailInterface(ABC):

    @abstractmethod
    def encrypt_email(self, email: str) -> str: pass
