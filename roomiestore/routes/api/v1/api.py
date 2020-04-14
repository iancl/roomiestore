from . import UserRoutes
from . import RouterBase
from roomiestore.config.constants import STATUS_NOT_FOUND, STATUS_ERROR
from flask import Flask


class API(RouterBase):
    def __init__(self, controllers, response_builder, logger):
        super().__init__(response_builder, logger)
        self._controllers = controllers
        self._users = UserRoutes(controllers.users, response_builder, logger)

    def mount(self, app: Flask):
        app.register_error_handler(STATUS_NOT_FOUND, self.respond_not_found)
        app.register_error_handler(STATUS_ERROR, self.respond_error)
        app.add_url_rule('/api/v1/healthcheck', methods=['GET'], view_func=self.health_check)

        self._users.mount(app)

    def health_check(self):
        return self.respond_health_check()

