from sqlalchemy import Column, String
from src.infra.db.settings.base import Base


class Users(Base):
    __tablename__ = "users"

    token = Column(String, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    device = Column(String, nullable=False)
    session_id = Column(String, nullable=False)
