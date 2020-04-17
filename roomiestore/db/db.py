from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DB:

    def __init__(self, config, logger):
        self._config = config
        self._logger = logger
        self._engine = create_engine(
            f'postgresql://{config["user"]}:{config["pass"]}@{config["host"]}:{config["port"]}/{config["db"]}')
        self._metadata = MetaData()

    @property
    def metadata(self):
        return self._metadata
