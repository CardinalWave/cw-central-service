from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.group import Group

class GroupCreate(ABC):

    @abstractmethod
    def create(self, group: Group) -> Group: Dict
