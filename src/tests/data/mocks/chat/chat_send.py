from typing import Dict
from src.domain.models.message import Message
from src.domain.models.session import Session
from src.domain.use_cases.chat.chat_send import ChatSend as ChatSendInterface


class ChatSendSpy(ChatSendInterface):
    @classmethod
    def send(cls, token: str, group_id: str, message: str) -> Dict:
        session = Session(session_id="session_idadsadasd", device="esp8266_01")
        return Message(group_id=group_id,
                       send_time="Mon, 08 Jul 2024 16:16:08 GMT",
                       payload=message,
                       username="test_username",
                       action="send",
                       session=session).to_dict()
