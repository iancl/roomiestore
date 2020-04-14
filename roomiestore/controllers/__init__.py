from .users import UserController


class Controller:
    def __init__(self, logger):
        self._logger = logger
        self._users = UserController(logger)

    @property
    def users(self):
        return self._users

