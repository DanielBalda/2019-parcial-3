class TaTeTi(object):
    def __init__(self, board = None):
        if not board:
            self.board = [' ' for _ in range(9)]
        else:
            self.board = board
    
    def validate(self, position):
        if 'x' in self.board[position-1] or 'o' in self.board[position-1]:
            return False
        return True

    def assign(self, position, element):
        if self.validate(position):
            self.board[position-1] = element
            return self.board
        else:
            raise Exception

    def win(self):
        pass

    def draw_board(self):
        pass

    def full(self):
        return ' ' not in self.board
