class UserController:
    def __init__(self, logger):
        self._logger = logger

    def get_user_by_id(self, user_id: int):
        self._logger.debug('get_user_by_id()')
        return {
            'name': 'TEST!'
        }