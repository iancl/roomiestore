from roomiestore.routes import API
from roomiestore.controllers import Controller
from roomiestore.utils.response_builder import ResponseBuilder
from .mocks.logger_mock import LoggerMock


def test_health_check(mocker):
    response_builder = ResponseBuilder()
    logger = LoggerMock()
    controllers = Controller(logger)
    api = API(controllers, response_builder, logger)
    spy = mocker.spy(api, 'respond_health_check')

    # should call method on parent class
    api.health_check()

    assert spy.call_count == 1, 'should have invoked healthcheck method from parent class'