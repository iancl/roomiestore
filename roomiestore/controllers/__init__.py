from .user import UserController
from .role import RoleController

from ..models import Role as RoleModel
from ..models import User as UserModel

class Controller:
    def __init__(self, logger, db):
        self._logger = logger
        self._db = db
        self._user = UserController(logger, db, UserModel)
        self._role = RoleController(logger, db, RoleModel)

    @property
    def user(self):
        return self._user

