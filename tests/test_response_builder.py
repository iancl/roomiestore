from roomiestore.utils.response_builder import ResponseBuilder

def test_success():
    expected = {'data': [1, 2, 3], 'status': 200, 'count': 3}
    model = ResponseBuilder.success([1, 2, 3])
    assert model == expected, 'success response object is not correct'

def test_not_found():
    expected = {'status': 404, 'message': 'foooo'}
    model = ResponseBuilder.not_found('foooo')
    assert model == expected, 'not found response is not correct'

def test_bad_request():
    expected = {'status': 400, 'message': 'foooo'}
    model = ResponseBuilder.bad_request('foooo')
    assert model == expected, 'bad request response is not correct'

def test_get_response_model():
    expected = { 'data': None, 'status': None, 'count': 0}
    model = ResponseBuilder.get_response_model()
    assert expected == model, 'base response model is incorrect'
