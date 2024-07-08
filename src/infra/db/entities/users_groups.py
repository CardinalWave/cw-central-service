from sqlalchemy import Column, String
from src.infra.db.settings.base import Base


class UsersGroups(Base):
    __tablename__ = "users_groups"

    id = Column(String, primary_key=True)
    secure_email = Column(String, nullable=False)
    user_token = Column(String, nullable=False)
    username = Column(String, nullable=False)
    group_title = Column(String, nullable=False)
    group_id = Column(String, nullable=False)
    updated_at = Column(String, nullable=False)
