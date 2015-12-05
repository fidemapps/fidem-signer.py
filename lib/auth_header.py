import re
import signature
from .util import headers, date


def parse(request=None):
    """
    Parse authorization header and return parameters.

    :param request:
    :return:
    """

    h = None
    if 'Authorization' in request['headers']:
        h = request['headers']['Authorization']
    elif 'authorization' in request['headers']:
        h = request['headers']['authorization']
    if not h:
        return None

    try:
        index = h.index(' ')
    except ValueError:
        return None

    params = _extract_parameters(h[index+1:])

    if 'Credential' not in params or params['Credential'] is None:
        return None
    if 'SignedHeaders' not in params or params['SignedHeaders'] is None:
        return None
    if 'Signature' not in params or params['Signature'] is None:
        return None

    params['scheme'] = h[0:index].strip()

    if 'scheme' not in params or params['scheme'] is None:
        return None

    return params


def _extract_parameters(header=None):
    """
    Extract parameters from header.

    :param header:
    :return:
    """

    sep = re.compile(r'(?: |,)')
    op = re.compile(r'=')

    head = sep.split(header)

    parameters = {}
    for item in head:
        parts = op.split(item)
        parts = map(lambda x: x.strip(), parts)
        if len(parts) == 2:
            parameters[parts[0]] = parts[1]
    return parameters


def format_auth_header(request=None, credentials=None):
    """
    Format auth header.

    :param request:
    :param credentials:
    :return:
    """

    signed_headers = headers.serialize_keys(request['headers'])
    scheme = "FIDEM4-HMAC-SHA256"
    datestr = date.strip_time(request['headers']['X-Fidem-Date'])

    lst = [
        scheme + " Credential=" + credentials['AccessKeyId'] + "/" + datestr + '/fidem',
        "SignedHeaders=" + headers.serialize_keys(request['headers']),
        "Signature=" + signature.generate(request, credentials, {
            'SignedHeaders': signed_headers,
            'scheme': scheme
        })
    ]
    return ', '.join(lst)
