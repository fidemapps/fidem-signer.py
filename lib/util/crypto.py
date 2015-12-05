import hmac
import hashlib


def hmac_digest(key=None, string=None, encoding=None):
    """
    Crypt using HMAC.

    :param key:
    :param string:
    :param encoding:
    :return:
    """

    h = hmac.new(key=key, digestmod=hashlib.sha256)
    h.update(unicode(string, 'utf-8'))
    if encoding:
        return h.hexdigest()
    return h.digest()


def hash_digest(string=None, encoding=None):
    """
    Hash using SHA256

    :param string:
    :param encoding:
    :return:
    """

    h = hashlib.sha256()
    h.update(unicode(string, 'utf-8'))
    if encoding:
        return h.hexdigest()
    return h.digest()
