

def normalize(request=None):
    """
    Normalize request to prevent bugs.

    :param request:
    :return:
    """

    request['headers'] = request['headers'] if 'headers' in request else {}
    return request
