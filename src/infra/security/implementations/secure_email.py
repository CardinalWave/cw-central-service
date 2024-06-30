import hashlib
from src.infra.security.interfaces.secure_email import SecureEmailInterface
from src.data.erros.domain_errors import BadRequestError, InternalServerError

class SecureEmail(SecureEmailInterface):
    def __init__(self) -> None:
        pass

    def encrypt_email(self, email: str) -> str:
        try:
            hash_sha256 = hashlib.sha256()
            hash_sha256.update(email.encode('utf-8'))
            encrypted_email = hash_sha256.hexdigest()
            return encrypted_email
        except BadRequestError as e:
            raise BadRequestError(str(e)) from e
        except Exception as e:
            raise InternalServerError(str(e)) from e
