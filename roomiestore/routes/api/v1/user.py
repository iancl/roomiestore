from .api_base import APIBase

# for typing purposes
from roomiestore.controllers.user import UserController


class UserRoutes(APIBase):
    def __init__(self, controller, response_builder, logger):
        super().__init__(response_builder, logger)
        self._controller: UserController = controller

    def mount(self, app):
        app.add_url_rule('/api/v1/users', methods=['GET'], view_func=self.get_user)

    def get_user(self):
        r = self._controller.get_user_by_id(1)
        return self.respond_success([r])


