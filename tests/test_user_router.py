import pytest
from roomiestore.routes.api.v1 import UserRoutes
from roomiestore.controllers.user import UserController
from .mocks.app_mock import AppMock
from roomiestore.utils.response_builder import ResponseBuilder



def test_mount(mocker):
    logger = {}
    app = AppMock()
    controller = UserController(logger)
    response_builder = ResponseBuilder()
    router = UserRoutes(controller, response_builder, logger)

    app_spy = mocker.spy(app, 'add_url_rule')
    router.mount(app)

    assert app_spy.call_count == 1, 'should be called once'
    assert app_spy.call_args[0][0] == '/api/v1/users', 'should use right endpoint path'
    assert app_spy.call_args[1] == {
        'methods': ['GET'], 'view_func': router.get_user }, 'should use right method and handler'


def test_get_user(mocker):
    '''
    TODO: update and test using a requestMock to pass test values
    '''
    logger = {}
    app = AppMock()
    controller = UserController(logger)
    response_builder = ResponseBuilder()
    router = UserRoutes(controller, response_builder, logger)
