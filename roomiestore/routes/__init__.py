from roomiestore.routes.api.v1 import API

class Router:
    def __init__(self, controllers, logger):
        self._controllers = controllers
        self._logger = logger
        self._api = API(controllers, logger)

    def mount(self, app):
        self._api.mount(app)
        self._logger.debug('MOUNTED ROUTER')