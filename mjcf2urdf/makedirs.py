import os
import six


def makedirs(name, mode=0o777, exist_ok=True):
    """An wrapper of os.makedirs that accepts exist_ok."""
    name = str(name)
    if six.PY2:
        try:
            os.makedirs(name, mode)
        except OSError:
            if not os.path.isdir(name):
                raise
    else:
        os.makedirs(name, mode, exist_ok=exist_ok)
