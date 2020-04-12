from roomiestore.utils.response_builder import ResponseBuilder
from roomiestore.config.constants import STATUS_SUCCESS, MIME_JSON
from flask import Response
import json


# this may look unnecessary but it's a way to centralize all the response generation to 1 place
class RouterBase:
    @staticmethod
    def respond_success(data_list):
        model = ResponseBuilder.success(data_list)
        return Response(json.dumps(model), mimetype=MIME_JSON, status=STATUS_SUCCESS)

