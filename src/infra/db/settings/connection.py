from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.config import Config


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = Config.CW_CENTRAL_DB

        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
