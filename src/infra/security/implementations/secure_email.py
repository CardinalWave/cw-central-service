from cryptography.fernet import Fernet
import base64
from src.infra.security.interfaces.secure_email import SecureEmail as SecureEmailInterface
from src.config.config import Config

class SecureEmail(SecureEmailInterface):
    def __init__(self) -> None:
        self.fernet = Fernet(Config.KEY)
    
    def encrypt_email(self, email: str) -> str:
        encrypted_email = self.fernet.encrypt(email.encode())
        encrypted_email_b64 = base64.urlsafe_b64decode(encrypted_email).decode()
        return encrypted_email_b64
    
    def decrypt_email(self, encrypted_email_b64: str) -> str:
        encrypted_email = base64.urlsafe_b64decode(encrypted_email_b64.encode())
        decrypted_email = self.fernet.decrypt(encrypted_email).decode()
        return decrypted_email
