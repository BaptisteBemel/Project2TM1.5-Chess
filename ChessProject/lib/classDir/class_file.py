from lib.utility.util import chessboard

class Piece:
    def __init__(self, name, color, dead, position):
        self.color = color
        self.name = name
        self.dead = dead
        self.position = position


class Pawn(Piece):
    def __init__(self, color):
        super().__init__("P", color, 0)
        self.nb_plays = 0


    def move(self, move_list):
        if len(move_list) != 2:       #Wrong move
            return 'error: 2 arguments needed'
        elif move_list[1] > 1 or move_list[0] > 2 or move_list[0] < 1 or move_list[1] < 0:
            return 'error: this move is impossible for a pawn'
        elif move_list[1] == 1:
            if move_list[0] == 1:      #If this kills another piece - no piece of the same color + piece of teh other color needed

            else:
                return 'error: this pawn cannot do this move'
        elif move_list[1] == 0:
            if move_list[0] == 2:
                if self.nb_plays == 0:      #First time this pawn plays, it can advance 2 cases if there is no piece where it wants to go

                elif self.nb_plays > 0:
                    return 'error: this pawn cannot do this move'
            if move_list[0] == 1:      #The pawn can play if there is no piece where it wants to go
        self.nb_plays = self.nb_plays + 1     #The pawn has played, it won't be its first play again


class Rook(Piece):
    def __init__(self, color):
        super().__init__("R", color, 0)


class Bishop(Piece):
    def __init__(self, color):
        super().__init__("B", color, 0)


class Queen(Piece):
    def __init__(self, color):
        super().__init__("Q", color, 0)


class Knight(Piece):
    def __init__(self, color):
        super().__init__("Kn", color, 0)


class King(Piece):
    def __init__(self, color):
        super().__init__("K", color, 0)

    def is_dead(self):
        if self.dead == 1:
            pass                    #must break the while loop


pieces = {'rook': {}, 'bishop': {}, 'pawn': {}, 'king': {}, 'knight': {}, 'queen': {}}


#Creation of the pieces instead of creating 32 objects one by one
def creation_pieces():
    for i in range(16):
        if i == 0:
            pieces['rook'][i] = Rook('white')
            pieces['bishop'][i] = Bishop('white')
            pieces['pawn'][i] = Pawn('white')
            pieces['knight'][i] = Knight('white')
            pieces['king'][i] = King('white')
            pieces['queen'][i] = Queen('white')
        elif i == 1:
            pieces['rook'][i] = Rook('white')
            pieces['bishop'][i] = Bishop('white')
            pieces['pawn'][i] = Pawn('white')
            pieces['knight'][i] = Knight('white')
            pieces['king'][i] = King('black')
            pieces['queen'][i] = Queen('black')
        elif i < 4:
            pieces['rook'][i] = Rook('black')
            pieces['bishop'][i] = Bishop('black')
            pieces['pawn'][i] = Pawn('white')
            pieces['knight'][i] = Knight('black')
        elif i < 8:
            pieces['pawn'][i] = Pawn('white')
        else:
            pieces['pawn'][i] = Pawn('black')
