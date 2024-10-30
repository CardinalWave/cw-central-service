from src.infra.security.implementations.secure_email import SecureEmail

def test_encrypy():

    secure_email = SecureEmail()

    email = "test@outlook.com.br"
    encrypt_email = secure_email.encrypt_email(email=email)

    assert encrypt_email != email
    assert len(encrypt_email) > len(email)
    assert len(encrypt_email) < 100
