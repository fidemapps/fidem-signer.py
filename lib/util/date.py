import datetime
from dateutil.parser import parse
import re


def to_iso_date_time(date=None):
    """
    Convert date in ISO datetime.

    :param date:
    :return:
    """

    try:
        dt = parse(date)
    except ValueError:
        dt = datetime.datetime.utcnow()
    string = re.sub(r'[:\-]|\.\d{6}', '', dt.isoformat())
    return "%sZ" % string


def strip_time(date=None):
    """
    Convert date in ISO date.

    :param date:
    :return:
    """

    try:
        dt = parse(date)
    except ValueError:
        dt = datetime.datetime.utcnow()
    string = re.sub(r'[:\-]|\.\d{6}', '', dt.isoformat())
    return string[0:8]
