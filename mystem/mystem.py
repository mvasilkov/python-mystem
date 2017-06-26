from subprocess import PIPE, Popen

from .capslock import MYSTEM
from .install import install, is_installed


class MyStem:
    '''
    Options:
        -h, -?               Print this synopsis and exit
        -v                   Print current version and exit
        -c                   Copy entire input to output
        -n                   Print every word on a new line
        -w                   Print only dictionary words
        -l                   Print only lemmas, without words
        -f                   Print lemma frequency. (Deprecated. Use --weight)
        -s                   Print end of sentence mark
                            (works only with -c)
        -i                   Print grammatical information
        -g                   Glue grammatical information for same lemmas in output
                            (works only with -i)
        -e <encoding>        Specify input/output encoding (UTF-8 by default)
        -d                   Apply disambiguation
        --eng-gr             Print grammems in English
        --filter-gram <list> List of accepted grammemes (comma-separated)
        --fixlist <file>     Use fixlist file
        --format <format>    Output format: text (default), xml, json
        --generate-all       Generate all possible hypotheses
        --weight             Print context-independent lemma weight
    '''

    def __init__(self, *, options=('-cs', '-i', '-d')):
        self._command = (str(MYSTEM), *options, '--format json')

    _process = None

    def _spawn_process(self):
        if not is_installed():
            install()

        self._process = Popen(
            self._command,
            stdin=PIPE,
            stdout=PIPE,
            bufsize=0,
            encoding='utf-8')

    def _is_running(self):
        return self._process is not None and self._process.poll() is not None

    def __del__(self):
        if self._is_running():
            self._process.terminate()
