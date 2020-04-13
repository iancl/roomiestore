from flask import request
from roomiestore.routes.api.v1.base import RouterBase
# for typing purposes
from roomiestore.controllers.users import UserController


class UserRoutes(RouterBase):
    def __init__(self, controller, logger):
        self._controller: UserController = controller
        self._logger = logger

    def mount(self, app):
        app.add_url_rule('/api/v1/users', methods=['GET'], view_func=self.get_user)

    def get_user(self):
        r = self._controller.get_user_by_id(1)
        return self.respond_success([r])


