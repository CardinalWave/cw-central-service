from sqlalchemy import Column, String
from src.infra.db.settings.base import Base

class Groups(Base):
    __tablename__ = "groups"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
