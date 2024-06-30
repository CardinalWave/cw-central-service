import hashlib
from src.infra.security.interfaces.secure_email import SecureEmailInterface
from src.data.erros.domain_errors import BadRequestError, InternalServerError

class SecureEmail(SecureEmailInterface):
    def __init__(self) -> None:
        pass
    
    def encrypt_email(self, email: str) -> str:
        try:
            hash = hashlib.sha256()
            hash.update(email.encode('utf-8'))
            encrypted_email = hash.hexdigest()
            print(f"Antes: {email}")
            print(f"Depois: {encrypted_email}")
            return encrypted_email
        except BadRequestError as e:
                raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e
