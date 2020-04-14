from roomiestore.controllers import UserController
from .mocks.logger_mock import LoggerMock


def test_get_users(mocker):
    logger = LoggerMock()
    controller = UserController(logger)
    expected = {'id': '1', 'name': 'foo'}

    spy = mocker.spy(controller, 'get_user_by_id')
    controller.get_user_by_id(1)

    assert spy.spy_return == expected, 'should have returned correct object'