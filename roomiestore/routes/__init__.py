from .api.v1 import API
from .app_router import AppRouter
from .base import RouterBase


class Router(RouterBase):
    def __init__(self, controllers, response_builder, logger):
        self._controllers = controllers
        self._logger = logger
        self._api = API(controllers, response_builder, logger)
        self._app_router = AppRouter(controllers, logger)

    def mount(self, app):
        self._app_router.mount(app)
        self._api.mount(app)
        self._logger.debug('MOUNTED ROUTER')