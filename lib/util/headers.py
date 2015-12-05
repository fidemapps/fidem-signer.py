import re


def serialize_keys(headers=None):
    """
    Serialize keys of the header.

    :param headers:
    :return:
    """
    valid = ['date', 'x-fidem-date']
    if not isinstance(headers, dict):
        headers = {}
    return ';'.join(sorted([x.lower() for x in headers.keys() if x.lower() in valid]))


def serialize(headers=None):
    """
    Serialize complete headers.

    :param headers:
    :return:
    """

    if not isinstance(headers, dict):
        headers = {}

    srt = sorted([x.lower() for x in headers.keys()])
    lst = map(lambda x: "%s:%s" % (x, headers[x]), srt)
    return '\n'.join(lst)


def filtered(headers=None, query=None):
    """
    Filter headers.

    :param headers:
    :param query:
    :return:
    """

    query = query.split(';')
    dico = {}
    for k in query:
        dico[k] = headers[k]
    return dico


def normalize(headers=None):
    """
    Lowercaseify all headers.

    :param headers:
    :return:
    """

    if not isinstance(headers, dict):
        headers = {}

    def _trim_all(header=None):
        stripped = (header + '').strip()
        return re.sub(r'\s+', ' ', stripped)

    trimmed = {}
    for key, value in headers.iteritems():
        trimmed[key.lower()] = _trim_all(value)
    return trimmed
