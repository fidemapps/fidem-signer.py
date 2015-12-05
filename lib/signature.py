import json
from .util import crypto, date, headers, path


def verify(request=None, credentials=None, parameters=None):
    """
    Verify a signature.

    :param request:
    :param credentials:
    :param parameters:
    :return:
    """

    return generate(request, credentials, parameters) == parameters['Signature']


def generate(request=None, credentials=None, parameters=None):
    """
    Generate a signature.

    :param request:
    :param credentials:
    :param parameters:
    :return:
    """

    h = headers.normalize(request['headers'])

    fidem_date_time = h['x-fidem-date']
    fidem_date = date.strip_time(fidem_date_time)
    key = crypto.hmac_digest('FIDEM' + credentials['SecretAccessKey'], fidem_date)

    path_parts = []
    try:
        path_parts = path.parse(request['path'])
    except KeyError:
        pass

    h = headers.filtered(h, parameters['SignedHeaders'])

    body = request['body'] if 'body' in request else '{}'
    if not isinstance(body, str):
        body = json.dumps(request['body'], separators=(',', ':'))

    lst = [
        request['method'] if 'method' in request else 'GET',
        path_parts[0] if len(path_parts) >= 1 else '/',
        path_parts[1] if len(path_parts) >= 2 else '',
        headers.serialize(h) + '\n',
        parameters['SignedHeaders'],
        crypto.hash_digest(body, 'hex')
    ]
    canonical_string = '\n'.join(lst)

    lst = [
        parameters['scheme'],
        fidem_date_time,
        credentials['AccessKeyId'] + '/' + fidem_date + '/fidem',
        crypto.hash_digest(canonical_string, 'hex')
    ]
    plain = '\n'.join(lst)

    return crypto.hmac_digest(key, plain, 'hex')
