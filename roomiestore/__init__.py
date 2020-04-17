from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

from roomiestore.routes import Router
from roomiestore.controllers import Controller
from roomiestore.utils.response_builder import ResponseBuilder
from roomiestore.db import DB

from sqlalchemy.exc import IntegrityError

class Application:
    def __init__(self, config):
        self._config = config
        self._server = Flask(__name__)
        self._logger = self._server.logger
        self._db = DB(config['db'], self._logger)
        self._response_builder = ResponseBuilder()
        self._controllers = Controller(self._logger, self._db)
        self._router = Router(self._controllers, self._response_builder, self._logger)

        # initializing all tables
        self._db.create_entities()

        # test
        import datetime
        from .models import User
        try:
            # self._controllers.user().add(
            #     fname='ian',
            #     lname='calderon',
            #     dob=datetime.datetime.strptime('03-29-1984', '%m-%d-%Y'),
            #     email='calderon.ian@gmail.com',
            #     phone=None,
            #     username='icalderon',
            #     passwd='123',
            #     role_id=1)

            r = self._db.query(User).filter_by(role_id=1).all()
            self._logger.error(r)
        except Exception as e:
            self._logger.error('===================>', e)


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
