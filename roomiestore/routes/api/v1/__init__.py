from roomiestore.routes.api.v1.users import UserRoutes

class API:
    def __init__(self, controllers, logger):
        self._logger = logger
        self._controllers = controllers
        self._users = UserRoutes(controllers.users, logger)

    def mount(self, app):
        self._users.mount(app)
        self._logger.debug('WOOOHOOO')