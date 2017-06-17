from pathlib import Path
import os
from shutil import copyfileobj
from subprocess import run, PIPE
import sys
import tarfile
from tempfile import TemporaryDirectory
from urllib.request import urlopen
from zipfile import ZipFile

from .capslock import (MYSTEM, MYSTEM_DIR, MYSTEM_VERSION_STRING, OS,
                       PACKAGES_ROOT, PACKAGES, RE_ARCHIVE)


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


def install_impl(bits=64):
    p = (OS, bits)
    if p not in PACKAGES:
        raise NotImplementedError()

    filetype = RE_ARCHIVE.search(PACKAGES[p]).group()
    winrar = ZipFile if filetype == '.zip' else tarfile.open

    with TemporaryDirectory() as dirname:
        filename = Path(dirname) / ('a' + filetype)
        url = PACKAGES_ROOT + PACKAGES[p]

        print('Downloading %s' % url, file=sys.stderr)
        print('Saving as %s' % filename, file=sys.stderr)

        with urlopen(url) as a, open(filename, 'wb') as b:
            copyfileobj(a, b)

        print('Extracting to %s' % MYSTEM_DIR, file=sys.stderr)

        with winrar(str(filename)) as a:
            a.extractall(str(MYSTEM_DIR))
