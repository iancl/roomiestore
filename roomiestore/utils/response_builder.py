from roomiestore.config.constants import STATUS_SUCCESS, STATUS_NOT_FOUND, STATUS_BAD_REQUEST, STATUS_ERROR


class ResponseBuilder:

    @staticmethod
    def success(data_list):
        model = ResponseBuilder.get_response_model()
        model['status'] = STATUS_SUCCESS
        model['data'] = data_list
        model['count'] = len(data_list)

        return model

    @staticmethod
    def not_found(message='resource not found'):
        model = ResponseBuilder.get_response_model()
        model['status'] = STATUS_NOT_FOUND
        model['message'] = message
        del model['data']
        del model['count']

        return model

    @staticmethod
    def bad_request(message='bad request'):
        model = ResponseBuilder.get_response_model()
        model['status'] = STATUS_BAD_REQUEST
        model['message'] = message
        del model['data']
        del model['count']

        return model

    @staticmethod
    def error(message='Unexpected error occurred'):
        model = ResponseBuilder.get_response_model()
        model['status'] = STATUS_ERROR
        model['message'] = message
        del model['data']
        del model['count']

        return model

    @staticmethod
    def get_response_model():
        return {
            'data': None,
            'status': None,
            'count': 0
        }
