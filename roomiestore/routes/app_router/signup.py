from . import AppRouterBase

# for typing purposes
from flask import Flask, render_template


class Signup(AppRouterBase):

    def __init__(self, controller, logger):
        self._controller = controller
        self._logger = logger

    def mount(self, app: Flask):
        app.add_url_rule('/signup', methods=['GET'], view_func=self.__signup)

    def __signup(self):
        params = {
            'title': 'signup',
            'navbar_title': 'Roomiestore Signup'
        }
        return render_template('signup/signup.html', **params)
