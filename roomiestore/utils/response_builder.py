from roomiestore.config.constants import STATUS_SUCCESS


class ResponseBuilder:
    @staticmethod
    def success(data_list):
        model = ResponseBuilder.get_response_model()
        model['status'] = STATUS_SUCCESS
        model['data'] = data_list
        model['count'] = len(data_list)

        return model

    @staticmethod
    def not_found(message):
        pass

    @staticmethod
    def bad_request(message):
        pass

    @staticmethod
    def get_response_model():
        return {
            'data': None,
            'status': None,
            'count': 0
        }
