import pytest
from roomiestore.routes.api.v1 import RouterBase
from roomiestore.utils.response_builder import ResponseBuilder


def test_respond_success(mocker):
    logger = {}
    response_builder = ResponseBuilder()

    expected_return = {'data': [1, 2, 3], 'status': 200, 'count': 3}

    spy = mocker.spy(response_builder, 'success')
    base = RouterBase(response_builder, logger)
    base.respond_success([1, 2, 3])

    assert spy.call_count == 1, 'should have been called once'
    assert spy.spy_return == expected_return, 'should have returned expected value'


def test_respond_not_found(mocker):
    logger = {}
    response_builder = ResponseBuilder()

    expected_return = {'status': 404, 'message': 'resource not found'}

    spy = mocker.spy(response_builder, 'not_found')
    base = RouterBase(response_builder, logger)
    base.respond_not_found('flask_default_message')

    assert spy.call_count == 1, 'should have been called once'
    assert spy.spy_return == expected_return, 'should have returned expected value'


def test_bad_request(mocker):
    logger = {}
    response_builder = ResponseBuilder()

    expected_return = {'status': 400, 'message': 'missing foo'}

    spy = mocker.spy(response_builder, 'bad_request')
    base = RouterBase(response_builder, logger)
    base.respond_bad_request('missing foo')

    assert spy.call_count == 1, 'should have been called once'
    assert spy.spy_return == expected_return, 'should have returned expected value'


def test_error(mocker):
    logger = {}
    response_builder = ResponseBuilder()

    expected_return = {'status': 500, 'message': 'Unexpected error occurred'}

    spy = mocker.spy(response_builder, 'error')
    base = RouterBase(response_builder, logger)
    base.respond_error('flask_default_message')

    assert spy.call_count == 1, 'should have been called once'
    assert spy.spy_return == expected_return, 'should have returned expected value'