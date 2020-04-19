from .app_router_base import AppRouterBase
from .dashboard import Dashboard
from .login import Login
from .signup import Signup

class AppRouter(AppRouterBase):
    def __init__(self, controllers, logger):
        self._controllers = controllers
        self._logger = logger
        # self._dashboard = Dashboard()
        self._login = Login(controllers.user, logger)
        self._signup = Signup(controllers.user, logger)

    def mount(self, app):
        self._login.mount(app)
        self._signup.mount(app)
