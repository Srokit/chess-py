"Board module that contains classes for the chess board"

from pieces import *

class Square:
    def __init__(self):
        self.piece = None
class Board:
    def __init__(self):
        "Fills the board with proper pieces"
        self.board = {}
