from lib.utility.util import chessboard, show_chessboard


class Piece:
    def __init__(self, name, color, dead, position = ""):
        self.color = color
        self.name = name
        self.dead = dead
        self.position = position


class Pawn(Piece):
    def __init__(self, color):
        super().__init__("P", color, 0)
        self.nb_plays = 0

    def __str__(self):
        return str(self.name)

    def move(self, move_list):
        if len(move_list) != 2:       #Wrong move
            return 'error: 2 arguments needed'
        elif move_list[1] > 1 or move_list[0] > 2 or move_list[0] < 1 or move_list[1] < 0:
            return 'error: this move is impossible for a pawn'
        elif move_list[1] == 1:
            if move_list[0] == 1:      #If this kills another piece - no piece of the same color + piece of the other color needed
                return True
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
        return str(self.name)


class Bishop(Piece):
    def __init__(self, color):
        super().__init__("B", color, 0)

    def __str__(self):
       return str(self.name)


class Queen(Piece):
    def __init__(self, color):
        super().__init__("Q", color, 0)

    def __str__(self):
        return str(self.name)


class Knight(Piece):
    def __init__(self, color):
        super().__init__("Kn", color, 0)

    def __str__(self):
        return str(self.name)


class King(Piece):
    def __init__(self, color):
        super().__init__("K", color, 0)

    def is_dead(self):
        if self.dead == 1:
            pass                    #must break the while loop

    def __str__(self):
        return str(self.name)


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
    """
    :param black_or_white: decide what is the color who is going to play the first player
    First we verify if it's white or black (or false value)
    Secondly we take every value in the pieces' dictonnary to implement them in their initial place
    Finally we put "x" value in the empty places
    """
    list_of_letter = ["a", "b", "c", "d", "e", "f", "g", "h"]
    if black_or_white == "white":
        key_in_pieces = pieces.keys()
        for names in key_in_pieces:
            id_in_names = pieces[names].keys()
            for id_ in id_in_names:
                if names == "rook":
                    if pieces[names][id_].color == "black":
                        if id_ % 2 == 0:
                            pieces[names][id_].position = "a1"
                            chessboard[1]["a"] = pieces[names][id_]
                        else:
                            pieces[names][id_].position = "h1"
                            chessboard[1]["h"] = pieces[names][id_]
                    else:
                        if id_ % 2 == 0:
                            pieces[names][id_].position = "a8"
                            chessboard[8]["a"] = pieces[names][id_]
                        else:
                            pieces[names][id_].position = "h8"
                            chessboard[8]["h"] = pieces[names][id_]
                elif names == "bishop":
                    if pieces[names][id_].color == "black":
                        if id_ % 2 == 0:
                            pieces[names][id_].position = "c1"
                            chessboard[1]["c"] = pieces[names][id_]
                        else:
                            pieces[names][id_].position = "f1"
                            chessboard[1]["f"] = pieces[names][id_]
                    else:
                        if id_ % 2 == 0:
                            pieces[names][id_].position = "c8"
                            chessboard[8]["c"] = pieces[names][id_]
                        else:
                            pieces[names][id_].position = "f8"
                            chessboard[8]["f"] = pieces[names][id_]
                elif names == "pawn":
                    if pieces[names][id_].color == "white":
                        if id_ < 8:
                            pieces[names][id_].position = list_of_letter[id_] + "7"
                            chessboard[7][list_of_letter[id_]] = pieces[names][id_]
                    else:
                        if id_ >= 8:
                            pieces[names][id_].position = list_of_letter[id_ - 8] + "2"
                            chessboard[2][list_of_letter[id_ - 8]] = pieces[names][id_]
                elif names == "king":
                    if pieces[names][id_].color == "black":
                        pieces[names][id_].position = "e1"
                        chessboard[1]["e"] = pieces[names][id_]
                    else:
                        pieces[names][id_].position = "e8"
                        chessboard[8]["e"] = pieces[names][id_]
                elif names == "queen":
                    if pieces[names][id_].color == "black":
                        pieces[names][id_].position = "d1"
                        chessboard[1]["d"] = pieces[names][id_]
                    else:
                        pieces[names][id_].position = "d8"
                        chessboard[8]["d"] = pieces[names][id_]
                elif names == "knight":
                    if pieces[names][id_].color == "black":
                        if id_ % 2 == 0:
                            pieces[names][id_].position = "b1"
                            chessboard[1]["b"] = pieces[names][id_]
                        else:
                            pieces[names][id_].position = "g1"
                            chessboard[1]["g"] = pieces[names][id_]
                    else:
                        if id_ % 2 == 0:
                            pieces[names][id_].position = "b8"
                            chessboard[8]["b"] = pieces[names][id_]
                        else:
                            pieces[names][id_].position = "g8"
                            chessboard[8]["g"] = pieces[names][id_]
        for numbers_x in range(3, 7):
            for numbers_in_letters in range(len(list_of_letter)):
                chessboard[numbers_x][numbers_in_letters] = "x"
    elif black_or_white == "black":
        key_in_pieces = pieces.keys()
        for names in key_in_pieces:
            id_in_names = pieces[names].keys()
            for id_ in id_in_names:
                if names == "rook":
                    if pieces[names][id_].color == "white":
                        if id_ % 2 == 0:
                            pieces[names][id_].position = "a1"
                            chessboard[1]["a"] = pieces[names][id_]
                        else:
                            pieces[names][id_].position = "h1"
                            chessboard[1]["h"] = pieces[names][id_]
                    else:
                        if id_ % 2 == 0:
                            pieces[names][id_].position = "a8"
                            chessboard[8]["a"] = pieces[names][id_]
                        else:
                            pieces[names][id_].position = "h8"
                            chessboard[8]["h"] = pieces[names][id_]
                elif names == "bishop":
                    if pieces[names][id_].color == "white":
                        if id_ % 2 == 0:
                            pieces[names][id_].position = "c1"
                            chessboard[1]["c"] = pieces[names][id_]
                        else:
                            pieces[names][id_].position = "f1"
                            chessboard[1]["f"] = pieces[names][id_]
                    else:
                        if id_ % 2 == 0:
                            pieces[names][id_].position = "c8"
                            chessboard[8]["c"] = pieces[names][id_]
                        else:
                            pieces[names][id_].position = "f8"
                            chessboard[8]["f"] = pieces[names][id_]
                elif names == "pawn":
                    if pieces[names][id_].color == "white":
                        if id_ < 8:
                            pieces[names][id_].position = list_of_letter[id_] + "2"
                            chessboard[2][list_of_letter[id_]] = pieces[names][id_]
                    else:
                        if id_ >= 8:
                            pieces[names][id_].position = list_of_letter[id_ - 8] + "7"
                            chessboard[7][list_of_letter[id_ - 8]] = pieces[names][id_]
                elif names == "king":
                    if pieces[names][id_].color == "white":
                        pieces[names][id_].position = "e1"
                        chessboard[1]["e"] = pieces[names][id_]
                    else:
                        pieces[names][id_].position = "e8"
                        chessboard[8]["e"] = pieces[names][id_]
                elif names == "queen":
                    if pieces[names][id_].color == "white":
                        pieces[names][id_].position = "d1"
                        chessboard[1]["d"] = pieces[names][id_]
                    else:
                        pieces[names][id_].position = "d8"
                        chessboard[8]["d"] = pieces[names][id_]
                elif names == "knight":
                    if pieces[names][id_].color == "white":
                        if id_ % 2 == 0:
                            pieces[names][id_].position = "b1"
                            chessboard[1]["b"] = pieces[names][id_]
                        else:
                            pieces[names][id_].position = "g1"
                            chessboard[1]["g"] = pieces[names][id_]
                    else:
                        if id_ % 2 == 0:
                            pieces[names][id_].position = "b8"
                            chessboard[8]["b"] = pieces[names][id_]
                        else:
                            pieces[names][id_].position = "g8"
                            chessboard[8]["g"] = pieces[names][id_]
        for numbers_x in range(3, 7):
            for numbers_in_letters in range(len(list_of_letter)):
                chessboard[numbers_x][numbers_in_letters] = "x"
    else:
        return "That's not a correct parameter (enter 'white' or 'black') !"


creation_pieces()
initial_game()
show_chessboard()
