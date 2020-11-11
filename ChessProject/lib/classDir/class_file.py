from lib.utility.util import chessboard


pieces = {'rook': {}, 'bishop': {}, 'pawn': {}, 'king': {}, 'knight': {}, 'queen': {}}


symbol_to_name = {'P': 'pawn', 'R': 'rook', 'B': 'bishop', 'Q': 'queen', 'N': 'knight', 'K': 'king'}


def whats_on_case(pos):
    kind_piece = chessboard[pos[0]][pos[1]]
    for piece in range(len(pieces[kind_piece])):
        if pieces[kind_piece][piece].position == pos[1] + str(pos[0]):
            return pieces[kind_piece][piece]
    return 'error: piece can not be found'


def get_position(piece_name, nb):
    list_position = sorted(pieces[piece_name][nb].position)
    return list_position


class Piece:
    def __init__(self, name, color, dead, id_piece, position=""):
        self.color = color
        self.name = name
        self.dead = dead
        self.position = position
        self.id_piece = id_piece


class Pawn(Piece):
    def __init__(self, color, id_piece):
        super().__init__("P", color, 0, id_piece)
        self.nb_plays = 0

    def __str__(self):
        return str(self.name)

    def move(self, move_list):                                      #move must be number then letter
        actual_position = get_position('pawn', self.id_piece)
        next_position = [int(actual_position[0]) + move_list[0], chr(ord(actual_position[1]) + move_list[1])]
        piece_next_case = whats_on_case(next_position)
        if len(move_list) != 2:                                    #Wrong move
            return 'error: 2 arguments needed'
        elif move_list[1] > 1 or move_list[0] > 2 or move_list[0] < 1 or move_list[1] < 0:
            return 'error: this move is impossible for a pawn'
        elif move_list[1] == 1:
            if move_list[0] == 1:                                  #If this kills another piece - no piece of the same color + piece of the other color needed
                if chessboard[next_position[0]][next_position[1]] == '.':
                    return 'error: this move is impossible for a pawn'
                elif piece_next_case.color == self.color:           #if that's the same color
                    return 'error: there is already another piece of the same color on this case'
                elif piece_next_case.color != self.color:              #Other color: it can kill it, the piece which moves take its position and the other disappears
                    self.position = next_position[1] + str(next_position[0])
                    piece_next_case.position = ''
                    chessboard[actual_position[0]][actual_position[1]] = '.'
                    chessboard[next_position[0]][next_position[1]] = self.name
                    self.nb_plays = self.nb_plays + 1                 #The pawn has played, it won't be its first play again
                    return chessboard
            else:
                return 'error: this pawn cannot do this move'
        elif move_list[1] == 0:
            if chessboard[next_position[0]][next_position[1]] != '.':  # Next position must be free
                return 'error: there is already another piece there'
            else:
                if move_list[0] == 2:
                    if self.nb_plays == 0:                              #First time this pawn plays, it can advance 2 cases
                        self.position = next_position[1] + str(next_position[0])
                        chessboard[actual_position[0]][actual_position[1]] = '.'
                        chessboard[next_position[0]][next_position[1]] = self.name
                        self.nb_plays = self.nb_plays + 1
                        return chessboard
                    elif self.nb_plays > 0:
                        return 'error: this pawn cannot do this move'
                if move_list[0] == 1:
                    self.position = next_position[1] + str(next_position[0])
                    chessboard[actual_position[0]][actual_position[1]] = '.'
                    chessboard[next_position[0]][next_position[1]] = self.name
                    self.nb_plays = self.nb_plays + 1
                    return chessboard


class Rook(Piece):
    def __init__(self, color, id_piece):
        super().__init__("R", color, 0, id_piece)

    def __str__(self):
        return str(self.name)


class Bishop(Piece):
    def __init__(self, color, id_piece):
        super().__init__("B", color, 0, id_piece)

    def __str__(self):
        return str(self.name)


class Queen(Piece):
    def __init__(self, color, id_piece):
        super().__init__("Q", color, 0, id_piece)

    def __str__(self):
        return str(self.name)


class Knight(Piece):
    def __init__(self, color, id_piece):
        super().__init__("N", color, 0, id_piece)

    def __str__(self):
        return str(self.name)


class King(Piece):
    def __init__(self, color, id_piece):
        super().__init__("K", color, 0, id_piece)

    def is_dead(self):
        if self.dead == 1:
            pass                    #must break the while loop

    def __str__(self):
        return str(self.name)

    def move(self, move):
        actual_pos = self.position
        #if move[]


#Creation of the pieces instead of creating 32 objects one by one
def creation_pieces():
    for i in range(16):
        if i == 0:
            pieces['rook'][i] = Rook('white', i)
            pieces['bishop'][i] = Bishop('white', i)
            pieces['pawn'][i] = Pawn('white', i)
            pieces['knight'][i] = Knight('white', i)
            pieces['king'][i] = King('white', i)
            pieces['queen'][i] = Queen('white', i)
        elif i == 1:
            pieces['rook'][i] = Rook('white', i)
            pieces['bishop'][i] = Bishop('white', i)
            pieces['pawn'][i] = Pawn('white', i)
            pieces['knight'][i] = Knight('white', i)
            pieces['king'][i] = King('black', i)
            pieces['queen'][i] = Queen('black', i)
        elif i < 4:
            pieces['rook'][i] = Rook('black', i)
            pieces['bishop'][i] = Bishop('black', i)
            pieces['pawn'][i] = Pawn('white', i)
            pieces['knight'][i] = Knight('black', i)
        elif i < 8:
            pieces['pawn'][i] = Pawn('white', i)
        else:
            pieces['pawn'][i] = Pawn('black', i)


def initial_game(black_or_white = "white"):
    """
    :param black_or_white: decide what is the color which is going to play the first player
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
    else:
        return "That's not a correct parameter (enter 'white' or 'black') !"
    for numbers_x in range(3, 7):
        for numbers_in_letters in list_of_letter:
            chessboard[numbers_x][numbers_in_letters] = "."

#creation_pieces()
#initial_game()
#show_chessboard()
