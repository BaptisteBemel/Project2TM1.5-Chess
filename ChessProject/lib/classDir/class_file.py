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
            if move_list[0] == 1:      #If this kills another piece - no piece of the same color + piece of the other color needed
<<<<<<< HEAD

=======
                return True
>>>>>>> 91f73ded3a1658d5af1176a9cbb21cfbd823ec84
            else:
                return 'error: this pawn cannot do this move'
        elif move_list[1] == 0:
            if move_list[0] == 2:
                if self.nb_plays == 0:      #First time this pawn plays, it can advance 2 cases if there is no piece where it wants to go
                    return True
                elif self.nb_plays > 0:
                    return 'error: this pawn cannot do this move'
            if move_list[0] == 1:      #The pawn can play if there is no piece where it wants to go
                return True
        self.nb_plays = self.nb_plays + 1     #The pawn has played, it won't be its first play again


class Rook(Piece):
    def __init__(self, color):
        super().__init__("R", color, 0)

    def __str__(self):
        return self.name


class Bishop(Piece):
    def __init__(self, color):
        super().__init__("B", color, 0)

    def __str__(self):
       return self.name


class Queen(Piece):
    def __init__(self, color):
        super().__init__("Q", color, 0)

    def __str__(self):
        return self.name


class Knight(Piece):
    def __init__(self, color):
        super().__init__("Kn", color, 0)

    def __str__(self):
        return self.name


class King(Piece):
    def __init__(self, color):
        super().__init__("K", color, 0)

    def is_dead(self):
        if self.dead == 1:
            pass                    #must break the while loop

    def __str__(self):
        return self.name



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

def initial_game(black_or_white = "white"):
    if black_or_white == "white":
        key_in_pieces = pieces.keys()
        for names in key_in_pieces:
            for id in range(len(names)):
                if names == "rook":
                    if pieces[names][id].color == "black":
                        if id % 2 == 0:
                            pieces[names][id].position = "a1"
                            chessboard[1]["a"] = pieces[names][id].name
                        else:
                            pieces[names][id].position = "h1"
                            chessboard[1]["h"] = pieces[names][id].name
                    else:
                        if id % 2 == 0:
                            pieces[names][id].position = "a8"
                            chessboard[8]["a"] = pieces[names][id].name
                        else:
                            pieces[names][id].position = "h8"
                            chessboard[8]["h"] = pieces[names][id].name
                elif names == "bishop":
                    if pieces[names][id].color == "black":
                        if id % 2 == 0:
                            pieces[names][id].position = "a1"
                            chessboard[1]["a"] = pieces[names][id].name
                        else:
                            pieces[names][id].position = "h1"
                            chessboard[1]["h"] = pieces[names][id].name
                    else:
                        if id % 2 == 0:
                            pieces[names][id].position = "a8"
                            chessboard[8]["a"] = pieces[names][id].name
                        else:
                            pieces[names][id].position = "h8"
                            chessboard[8]["h"] = pieces[names][id].name



    elif black_or_white == "black":

    else:
        return "That's not a correct parameter (enter 'white' or 'black') !"