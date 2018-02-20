import sys

import os

from colors import magenta


class View():
    new_line_char = '\n'

    def __init__(self):
        pass

    @classmethod
    def print_(cls, string_, new_line=True):
        if not new_line:
            cls.new_line_char = ''

        sys.stdout.write(string_ + cls.new_line_char)
        sys.stdout.flush()

    @classmethod
    def clear_screen(cls):
        os.system('clear')

    @classmethod
    def print_title(cls, title):
        cls.print_('')
        cls.print_(magenta(title))
        cls.print_(magenta('--------------------------'))
