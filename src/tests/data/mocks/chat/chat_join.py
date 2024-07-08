from typing import Dict

from src.domain.models.group import Group

from src.domain.use_cases.chat.chat_join import ChatJoin as ChatJoinInterface


class ChatJoinSpy(ChatJoinInterface):

    def join(self, group_id: str, token: str) -> Dict:
        return Group(group_id=group_id, title="GroupTest").to_dict()
