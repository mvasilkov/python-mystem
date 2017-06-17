from pathlib import Path
import platform
import re

PACKAGES_ROOT = 'http://download.cdn.yandex.net/mystem/'

PACKAGES = {
    ('Darwin', 64): 'mystem-3.0-macosx10.8.tar.gz',

    # ('FreeBSD', 64): 'mystem-3.0-freebsd9.0-64bit.tar.gz',
    ('FreeBSD', 64): 'mystem-3.0-freebsd9.2-64bit.tar.gz',

    ('Linux', 64): 'mystem-3.0-linux3.1-64bit.tar.gz',
    ('Linux', 32): 'mystem-3.0-linux3.5-32bit.tar.gz',

    ('Windows', 64): 'mystem-3.0-win7-64bit.zip',
    ('Windows', 32): 'mystem-3.0-win7-32bit.zip',
}

RE_ARCHIVE = re.compile('(\.tar\.gz|\.zip)$')

OS = platform.system()

MSDOS = OS == 'Windows'

OUR_ROOT = Path(__file__).parent.resolve()

MYSTEM_DIR = OUR_ROOT / 'bin'

MYSTEM_EXE = 'mystem.exe' if MSDOS else 'mystem'

MYSTEM = MYSTEM_DIR / MYSTEM_EXE

MYSTEM_VERSION_STRING = 'Mystem 3.0\n'
