from collections import namedtuple
from pathlib import Path
import platform
import re

PACKAGES_ROOT = 'https://download.cdn.yandex.net/mystem/'

pkg = namedtuple('pkg', ('name', 'size', 'sha224'))

PACKAGES = {
    ('Darwin', 64):
    pkg('mystem-3.0-macosx10.8.tar.gz', 16544177,
        '703d2941bb18361832a0f28c94d27e350270fdb96783d0a675253ddc'),
    # ('FreeBSD', 64):
    # pkg('mystem-3.0-freebsd9.0-64bit.tar.gz', 16468557,
    #     '122eb6d1675aef0e01c595050b6d6ca5172303dca67ada1a49339821'),
    ('FreeBSD', 64):
    pkg('mystem-3.0-freebsd9.2-64bit.tar.gz', 16432750,
        '73a3308f1276b3a686d8ac6578edf1f8afefa4174902caa38204f729'),
    ('Linux', 64):
    pkg('mystem-3.0-linux3.1-64bit.tar.gz', 16457938,
        'ce434643cf693cdd139436156d55feb92105c02c7e597ba06bcebc13'),
    ('Linux', 32):
    pkg('mystem-3.0-linux3.5-32bit.tar.gz', 16527292,
        'f07ab160184dea1bb662e8eff47adadd782e4d62c840f22dea3f872f'),
    ('Windows', 64):
    pkg('mystem-3.0-win7-64bit.zip', 16564096,
        '4ec3b1cdddf2b9b3238d59e01100a22474f5a755555e43df919416e3'),
    ('Windows', 32):
    pkg('mystem-3.0-win7-32bit.zip', 16266428,
        '198fb009758e173e57f6519108ef7309f36d3eca5aae265e2b782dfa'),
}

RE_ARCHIVE = re.compile('(\.tar\.gz|\.zip)$')

OS = platform.system()

MSDOS = OS == 'Windows'

OUR_ROOT = Path(__file__).parent.resolve()

MYSTEM_DIR = OUR_ROOT / 'bin'

MYSTEM_EXE = 'mystem.exe' if MSDOS else 'mystem'

MYSTEM = MYSTEM_DIR / MYSTEM_EXE

MYSTEM_VERSION_STRING = 'Mystem 3.0\n'
