import board
import re


class Game:
    def __init__(self):
        self.guess_board = None
        self.code_board = Board
        self.colors = Enum('Color', ['RED', 'ORANGE', 'YELLOW', 'PINK', 'GREEN', 'BLUE', 'WHITE', 'BLACK'])
        self.guess_received = False

    def guess(self):
        guard = true
        while guard:
            i = input("Guess the color in order: ")
            if re.match(i, r''):
                self.guess_board = Board(i)

    def check_board(self):
        if self.code_board == self.guess_board:
            return True
        pass

    def answer(self):
        pass