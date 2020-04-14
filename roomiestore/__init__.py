from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

from roomiestore.routes import Router
from roomiestore.controllers import Controller
from roomiestore.utils.response_builder import ResponseBuilder

class Application:
    def __init__(self, config):
        self._config = config
        self._server = Flask(__name__)
        self._logger = self._server.logger
        self._response_builder = ResponseBuilder()
        self._controllers = Controller(self._logger)
        self._router = Router(self._controllers, self._response_builder, self._logger)

    def setup_logging(self):
        level = logging.DEBUG if self._config['logging']['level'] == 'DEBUG' else logging.INFO
        formatter = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s]: %(message)s')
        # Limit the size to 1000000Bytes ~ 1MB
        file_handler = RotatingFileHandler('log.log', maxBytes=1000000, backupCount=5)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        self._logger.setLevel(level)
        self._logger.addHandler(file_handler)

    def mount_routes(self):
        self._router.mount(self._server)

    @property
    def server(self):
        return self._server
