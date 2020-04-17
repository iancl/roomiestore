from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class DB:
    def __init__(self, config, logger):
        self._engine = create_engine(
            f'postgresql://{config["user"]}:{config["pass"]}@{config["host"]}:{config["port"]}/{config["db"]}')
        self._connection = self._engine.connect()
        self._logger = logger
        DBSession = sessionmaker(bind=self._engine)
        self._session = DBSession()

    def create_entities(self):
        Base.metadata.create_all(self._engine)

    def add(self, obj):
        '''
        raises IdentityError
        '''
        self._session.add(obj)
        self._session.commit()

    def query(self, cls):
        return self._session.query(cls)
