import http.client
import json
from src.domain.use_cases.user_authenticator import UserAuthenticatorInterface
from src.domain.models.user import User
from src.domain.models.login import Login
from src.domain.models.register import Register

class UserAuthenticator(UserAuthenticatorInterface):
    cw_auth_service = ""

    @classmethod
    def login(cls, login: Login) -> User:
        url = cls.cw_auth_service
        request = cls._request_auth(params=login, url=url, action="login")
        return request

    @classmethod
    def register(cls, register: Register) -> User:
        url = cls.cw_auth_service
        request = cls._request_auth(params=register.to_json(), url=url, action="regiter")
        return request
    
    def _request_auth(params: any, url, action) -> User:
        try:
            headers = {
                'Content-type': 'application/json'
            }

            conn = http.client.HTTPConnection(url)
            conn.request("POST", f"/user/"+action, params, headers)
            response = conn.getresponse()
            if response.status != 200:
                raise ValueError("Request error")

            data = response.read()
            json_data = json.loads(data)
            conn.close()

            return User(token=json_data['token'][0], username=json_data['username'], email=json_data['email'])
        except Exception as error:
            raise ValueError(f"Return error {error}")

