"Pieces module that contains the classes of the chess pieces"

class Piece:
    "Base class for all chess pieces"
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
    def move(self):
        "To be implemented in derived classes"
        pass
    
class Rook(Piece):
    def check_move(self, start_pos, end_pos):
        "Move in an L shape"
        if direction is "up right":
            self.y -= 2
            self.x += 1
        elif direction is "up left":
            self.y -= 2
