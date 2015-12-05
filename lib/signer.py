from .util import date, request
import auth_header
import signature


def verify(req=None, credentials=None):
    """
    Verify a request.

    :param req:
    :param credentials:
    :return:
    """

    req = request.normalize(req)
    params = auth_header.parse(req)
    if not params:
        return False

    return signature.verify(req, credentials, params)


def sign(req=None, credentials=None):
    """
    Sign a request.

    :param req:
    :param credentials:
    :return:
    """

    req = request.normalize(req)
    if 'Date' in req['headers']:
        req['headers']['X-Fidem-Date'] = date.to_iso_date_time(
            req['headers']['Date']
        )
    elif 'date' in req['headers']:
        req['headers']['X-Fidem-Date'] = date.to_iso_date_time(
            req['headers']['date']
        )

    req['headers']['Authorization'] = auth_header.format_auth_header(req, credentials)
    return req
