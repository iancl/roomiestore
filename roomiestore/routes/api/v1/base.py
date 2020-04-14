from roomiestore.config.constants import STATUS_SUCCESS, STATUS_NOT_FOUND, STATUS_ERROR, STATUS_BAD_REQUEST, \
    MIME_JSON, MIME_TEXT

from flask import Response
import json


# this may look unnecessary but it's a way to centralize all the response generation to 1 place
class RouterBase:
    '''
    Adds methods to respond requests to child classes
    '''

    def __init__(self, response_builder, logger):
        self._response_builder = response_builder
        self._logger = logger

    def respond_success(self, data_list):
        model = self._response_builder.success(data_list)
        return Response(json.dumps(model), mimetype=MIME_JSON, status=STATUS_SUCCESS)

    def respond_not_found(self, default_message):
        model = self._response_builder.not_found()
        return Response(json.dumps(model), mimetype=MIME_JSON, status=STATUS_NOT_FOUND)

    def respond_error(self, default_message):
        model = self._response_builder.error()
        return Response(json.dumps(model), mimetype=MIME_JSON, status=STATUS_ERROR)

    def respond_bad_request(self, message):
        model = self._response_builder.bad_request(message)
        return Response(json.dumps(model), mimetype=MIME_JSON, status=STATUS_BAD_REQUEST)

    @staticmethod
    def respond_health_check():
        return Response(mimetype=MIME_TEXT, status=STATUS_SUCCESS)

