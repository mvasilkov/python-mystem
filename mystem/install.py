import os
from subprocess import run, PIPE

from .capslock import MYSTEM, MYSTEM_VERSION_STRING


def is_installed():
    return MYSTEM.is_file() and os.access(MYSTEM, os.X_OK)


def is_usable():
    if is_installed():
        try:
            a = run('%s -v' % MYSTEM, stdout=PIPE, encoding='utf-8')
            return a.stdout == MYSTEM_VERSION_STRING
        except OSError:
            pass

    return False
