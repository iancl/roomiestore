from . import AppRouterBase

# for typing purposes
from flask import Flask, render_template

class Login(AppRouterBase):

    def __init__(self, controller, logger):
        self._controller = controller
        self._logger = logger

    def mount(self, app: Flask):
        app.add_url_rule('/login', methods=['GET'], view_func=self.__login)

    def __login(self):
        params = {
            'title': 123,
            'navbar_title': 'Roomiestore Login'
        }
        return render_template('login/login.html', **params)
