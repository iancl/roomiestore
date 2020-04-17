class RoleController:
    def __init__(self, logger, db, RoleModel):
        self._logger = logger
        self._db = db
        self._Model = RoleModel

    def get_by_id(self, role_id):
        pass
