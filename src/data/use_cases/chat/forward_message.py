import datetime
from typing import Dict

from src.domain.models.group import Group
from src.domain.models.user import User
from src.domain.use_cases.chat.forward_message import ForwardMessage as ForwardMessageInterface

class ForwardMessage(ForwardMessageInterface):

    def join_group(self, user: User, group: Group, updated_at: datetime): pass

    def send_message(self, user: User, group: Group, message: Dict): pass

    def logout_group(self, user: User, group: Group, updated_at: datetime): pass