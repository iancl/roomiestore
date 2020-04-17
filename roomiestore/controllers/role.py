# for typing purposes
from ..db import DB


class RoleController:
    def __init__(self, logger, db, role_model):
        self._logger = logger
        self._db: DB = db
        self._Model = role_model

    def get_by_id(self, role_id):
        return self._db.query(self._Model).filter_by(role_id=role_id).all()

    def add(self, name, description):
        role = self._Model(name=name, description=description)
        self._db.add(role)

