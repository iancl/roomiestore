class UserController:
    def __init__(self, logger, db, UserModel):
        self._logger = logger
        self._db = db
        self._Model = UserModel

    def get_user_by_id(self, user_id: int):
        self._logger.debug('get_user_by_id()')
        return {
            'id': '1',
            'name': 'foo'
        }