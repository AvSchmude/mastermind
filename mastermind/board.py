from enum import Enum


class Board:
    def __int__(self, col: list = None):
        if col is None:
            self.code_position = [None, None, None, None, None]
        else:
            self.code_position = col
        self.tip_position = []