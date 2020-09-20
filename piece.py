class Piece:

    movement = (0,0)

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color  # 0 for white, 1 for black

    def movement(self, x_move, y_move, game_array):
        global pieces_between
        pieces_between = 0
        # orthogonal y
        if self.x == x_move:

            for i in range(y_move - self.y):
                if(game_array[i][self.x] != None):
                    pieces_between = 1

        # orthogonal x
        elif self.y == y_move:
            for i in range(y_move - self.y):
                if (game_array[i][self.x] != None):
                    pieces_between = 1

        if pieces_between == 1:
            return "ERROR: pieces between."
        else:
            self.x = x_move
            self.y = y_move


class Pawn(Piece):
    movement = (0,1)

