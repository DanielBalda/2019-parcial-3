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
        if self.board[0] != ' ' and self.board[0] ==  self.board[3] and self.board[3] == self.board[6] and self.board[0] ==  self.board[6]:
            return True
        elif self.board[1] != ' ' and self.board[1] ==  self.board[4] and self.board[4] == self.board[7] and self.board[1] ==  self.board[7]:
            return True
        elif self.board[2] != ' ' and self.board[2] ==  self.board[5] and self.board[5] == self.board[8] and self.board[2] ==  self.board[8]:
            return True
        elif self.board[0] != ' ' and self.board[0] ==  self.board[1] and self.board[1] == self.board[2] and self.board[0] ==  self.board[2]:
            return True
        elif self.board[3] != ' ' and self.board[3] ==  self.board[4] and self.board[4] == self.board[5] and self.board[3] ==  self.board[5]:
            return True
        elif self.board[6] != ' ' and self.board[6] ==  self.board[7] and self.board[7] == self.board[8] and self.board[6] ==  self.board[8]:
            return True
        elif self.board[0] != ' ' and self.board[0] ==  self.board[4] and self.board[4] == self.board[8] and self.board[0] ==  self.board[8]:
            return True
        elif self.board[2] != ' ' and self.board[2] ==  self.board[4] and self.board[4] == self.board[6] and self.board[2] ==  self.board[6]:
            return True
        else:
            return False


    def draw_board(self):
        printing = "\n"
        for num in range(9):
            if self.board[num] != " ":
                printing += " " + self.board[num] + " "
            else:
                printing += " " + str(1+num) + " "
            if num == 2 or num == 5:
                printing += "\n---+---+---\n"
            elif num == 8:
                printing += "\n"
            else:
                printing += "|"
        return printing

    def full(self):
        return ' ' not in self.board
