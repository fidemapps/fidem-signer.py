

def parse(path=None):
    """
    Parse path.

    :param path:
    :return:
    """

    if not path:
        path = '/'
    return path.split('?')
