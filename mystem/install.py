import os
import re
import sys
import tarfile
from hashlib import sha224
from pathlib import Path
from subprocess import PIPE, run
from tempfile import TemporaryDirectory
from urllib.request import urlopen
from zipfile import ZipFile

from .capslock import (MYSTEM, MYSTEM_DIR, MYSTEM_VERSION_STRING, OS, PACKAGES,
                       PACKAGES_ROOT)


def is_installed():
    # return MYSTEM.is_file() and os.access(MYSTEM, os.X_OK)
    return os.access(MYSTEM, os.F_OK | os.X_OK)


def is_usable():
    if is_installed():
        try:
            a = run((str(MYSTEM), '-v'), stdout=PIPE, encoding='utf-8')
            return a.stdout == MYSTEM_VERSION_STRING
        except OSError:
            pass

    return False


def install_impl(bits=64):
    p = (OS, bits)
    if p not in PACKAGES:
        raise NotImplementedError()

    pkg = PACKAGES[p]
    filetype = re.search('(\.tar\.gz|\.zip)$', pkg.name).group()
    winrar = ZipFile if filetype == '.zip' else tarfile.open

    with TemporaryDirectory() as dirname:
        filename = Path(dirname) / ('pkg' + filetype)
        url = PACKAGES_ROOT + pkg.name

        print('Downloading %s' % url, file=sys.stderr)
        print('Saving as %s' % filename, file=sys.stderr)

        with urlopen(url) as a, open(filename, 'wb') as b:
            size, checksum = copyfileobj(a, b)

        assert size == pkg.size, 'Incomplete download'
        assert checksum == pkg.sha224, 'Corrupt download'

        print('Extracting to %s' % MYSTEM_DIR, file=sys.stderr)

        # ZipFile before 3.6.2 required str()
        with winrar(str(filename)) as a:
            a.extractall(str(MYSTEM_DIR))


def copyfileobj(a, b):
    size = 0
    checksum = sha224()
    progress = 0

    while 1:
        buf = a.read(64 * 1024)
        if not buf:
            break

        b.write(buf)
        size += len(buf)
        checksum.update(buf)

        size_mb = size // 2**20
        if size_mb > progress:
            progress = size_mb
            sys.stderr.write('.')
            sys.stderr.flush()

    print('Done', file=sys.stderr)
    return (size, checksum.hexdigest())
