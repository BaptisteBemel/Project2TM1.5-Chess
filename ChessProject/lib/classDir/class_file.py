from lib.utility.util import *


pieces = {'rook': {}, 'bishop': {}, 'pawn': {}, 'king': {}, 'knight': {}, 'queen': {}}


symbol_to_name = {'P': 'pawn', 'R': 'rook', 'B': 'bishop', 'Q': 'queen', 'N': 'knight', 'K': 'king'}


def whats_on_case(pos):
    position = sorted(pos)
    position[0] = int(position[0])
    kind_piece = chessboard[position[0]][position[1]]
    if kind_piece == '.':
        return kind_piece
    else:
        kind_piece = symbol_to_name[str(kind_piece)]
        for piece in range(len(pieces[kind_piece].keys())):
            if pieces[kind_piece][piece].position == pos:
                return pieces[kind_piece][piece]
    print('error: piece can not be found')


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


    def move(self, next_position):
        actual_position = convert_to_list(pieces['pawn'][self.id_piece].position)
        list_actual_position = sorted(pieces['pawn'][self.id_piece].position)
        list_actual_position[0] = int(list_actual_position[0])
        piece_next_case = whats_on_case(next_position)
        list_next_position = sorted(next_position)
        list_next_position[0] = int(list_next_position[0])
        next_position = convert_to_list(next_position)
        move_list = [next_position[0] - actual_position[0], next_position[1] - actual_position[1]]    #deplacement in columns then lines
        if self.color == 'white' and move_list[0] > -1:
            print('error: the pawn cannot move back')
        elif self.color == 'black' and move_list[0] < 1:
            print('error: the pawn cannot move back')
        else:
            move_list_abs = [abs(move_list[0]), abs(move_list[1])]
            if len(move_list_abs) != 2:                                    #Wrong move
                print('error: 2 arguments needed')
            elif move_list_abs[1] > 1 or move_list_abs[0] > 2 or move_list_abs[0] < 1 or move_list_abs[1] < 0:
                print('error: this move is impossible for a pawn')
            elif move_list_abs[1] == 1:
                if move_list_abs[0] == 1:                                  # If this kills another piece - no piece of the same color + piece of the other color needed
                    if chessboard[next_position[0]][list_next_position[1]] == '.':
                        print('error: this move is impossible for a pawn')
                    elif piece_next_case.color == self.color:           # if that's the same color
                        print('error: there is already another piece of the same color on this case')
                    elif piece_next_case.color != self.color:              # Other color: it can kill it, the piece which moves take its position and the other disappears
                        self.position = list_next_position[1] + str(list_next_position[0])
                        piece_next_case.position = ''
                        chessboard[list_next_position[0]][list_next_position[1]] = chessboard[list_actual_position[0]][list_actual_position[1]]
                        chessboard[list_actual_position[0]][list_actual_position[1]] = '.'
                        self.nb_plays = self.nb_plays + 1                 # The pawn has played, it won't be its first play again
                        return chessboard
                else:
                    print('error: this pawn cannot do this move')
            elif move_list_abs[1] == 0:
                if chessboard[list_next_position[0]][list_next_position[1]] != '.':  # Next position must be free
                    print('error: there is already another piece there')
                else:
                    if move_list_abs[0] == 2:
                        if self.nb_plays == 0:                              # First time this pawn plays, it can advance 2 cases
                            self.position = list_next_position[1] + str(list_next_position[0])
                            chessboard[list_next_position[0]][list_next_position[1]] = chessboard[list_actual_position[0]][list_actual_position[1]]
                            chessboard[list_actual_position[0]][list_actual_position[1]] = '.'
                            self.nb_plays = self.nb_plays + 1
                            return chessboard
                        elif self.nb_plays > 0:
                            print('error: this pawn cannot do this move')
                    if move_list_abs[0] == 1:
                        self.position = list_next_position[1] + str(list_next_position[0])
                        chessboard[list_next_position[0]][list_next_position[1]] = chessboard[list_actual_position[0]][list_actual_position[1]]
                        chessboard[list_actual_position[0]][list_actual_position[1]] = '.'
                        self.nb_plays = self.nb_plays + 1
                        return chessboard


class Rook(Piece):
    def __init__(self, color, id_piece):
        super().__init__("R", color, 0, id_piece)

    def __str__(self):
        return str(self.name)

    def move(self, move_on_chessboard):
        move = convert_to_list(move_on_chessboard)  # Convert the string (example 'h8') in list '[8, 7]
        actual_position = self.position
        alpha_string = "abcdefgh"
        if_exit(move)
        max_value = 0
        min_value = 0
        is_good_way = True
        while True:
            # Verify if it's a good translation for the rook
            if ((move[0] != actual_position[1]) & (alpha_string[move[1]] != actual_position[0])) | ((move[0] == actual_position[1]) & (alpha_string[move[1]] == actual_position[0])):
                print("The value is the same of the position of the object or your rook can not move the abscissa and \
                the ordinate at the same time")
                retry = input("Choose an another position : ")
                if_exit(retry)
                move = convert_to_list(verify_position(retry))
            # Verify if the position where the object is moving is used by an other object with an opposite color
            elif (chessboard[move[0]][alpha_string[move[1]]] != ".") & (chessboard[move[0]][alpha_string[move[1]]].color == self.color):
                print("The color of the object on the position entered is the same")
                retry = input("Choose an another position : ")
                if_exit(retry)
                move = convert_to_list(verify_position(retry))
            # Verify if the object is moving on the abscissa
            elif (move[0] != actual_position[1]) & (alpha_string[move[1]] == actual_position[0]):
                if move[0] > int(actual_position[1]):
                    max_value = move[0]
                    min_value = int(actual_position[1])
                else:
                    max_value = int(actual_position[1])
                    min_value = move[0]
                # Verify if there is something on the way of the rook
                for ordonate in range(min_value + 1, max_value):
                    if chessboard[ordonate][actual_position[0]] != ".":
                        is_good_way = False
                        print("There is an object on the way of the rook !")
                        retry = input("Choose an another position : ")
                        if_exit(retry)
                        move = convert_to_list(verify_position(retry))
                if is_good_way is True:
                    chessboard[move[0]][alpha_string[move[1]]] = chessboard[actual_position[1]][actual_position[0]]
                    chessboard[actual_position[1]][actual_position[0]] = "."
                    chessboard[move[0]][alpha_string[move[1]]].position = str(alpha_string[move[1]]) + str(move[0])
                    return 1
            # Verify if the object is moving on the ordonate
            elif (move[0] == actual_position[1]) & (alpha_string[move[1]] != actual_position[0]):
                number_actual = 0
                number = 0
                for letter in range(8):
                    if alpha_string[letter] == move[1]:
                        number = letter
                        break
                for letter in range(8):
                    if alpha_string[letter] == actual_position[0]:
                        number_actual = letter
                        break
                if number > number_actual:
                    max_value = number
                    min_value = number_actual
                else:
                    max_value = number_actual
                    min_value = number
                # Verify if there is something on the way of the rook
                for abscissa in range(min_value, max_value):
                    if chessboard[actual_position[1]][alpha_string[abscissa]] != ".":
                        is_good_way = False
                        print("There is an object on the way of the rook !")
                        retry = input("Choose an another position : ")
                        if_exit(retry)
                        move = convert_to_list(verify_position(retry))
                if is_good_way is True:
                    chessboard[move[0]][alpha_string[move[1]]] = chessboard[actual_position[1]][actual_position[0]]
                    chessboard[actual_position[1]][actual_position[0]] = "."
                    chessboard[move[0]][alpha_string[move[1]]].position = str(alpha_string[move[1]]) + str(move[0])
                    return 1


class Bishop(Piece):
    def __init__(self, color, id_piece):
        super().__init__("B", color, 0, id_piece)


    def move(self, next_position):

        actual_position = convert_to_list(pieces['bishop'][self.id_piece].position)
        list_actual_position = sorted(pieces['bishop'][self.id_piece].position)
        list_actual_position[0] = int(list_actual_position[0])
        piece_next_case = whats_on_case(next_position)
        list_next_position = sorted(next_position)
        list_next_position[0] = int(list_next_position[0])
        next_position = convert_to_list(next_position)
        move_list = [next_position[0] - actual_position[0], next_position[1] - actual_position[1]]
        move_list_abs = [abs(next_position[0] - actual_position[0]), abs(next_position[1] - actual_position[1])]
        sth_on_way = False

        if move_list[0] > 0:
            if move_list[1] > 0:
                for case in range(1, move_list_abs[0]):
                    if chessboard[list_actual_position[0] + case][chr(ord(list_actual_position[1]) + case)] != '.':
                        sth_on_way = True
            elif move_list[1] < 0:
                for case in range(1, move_list_abs[0]):
                    if chessboard[list_actual_position[0] + case][chr(ord(list_actual_position[1]) - case)] != '.':
                        sth_on_way = True
        elif move_list[0] < 0:
            if move_list[1] < 0:
                for case in range(1, move_list_abs[0]):
                    if chessboard[list_actual_position[0] - case][chr(ord(list_actual_position[1]) - case)] != '.':
                        sth_on_way = True
            elif move_list[1] > 0:
                for case in range(1, move_list_abs[0]):
                    if chessboard[list_actual_position[0] - case][chr(ord(list_actual_position[1]) + case)] != '.':
                        sth_on_way = True

        if move_list_abs[0] != move_list_abs[1]: #must be a diagonal
            print('error: the bishop cannot do this move')
        elif sth_on_way:
            print('error: something is on the way')
        else:
            if piece_next_case == '.':
                self.position = list_next_position[1] + str(list_next_position[0])
                chessboard[list_next_position[0]][list_next_position[1]] = chessboard[list_actual_position[0]][list_actual_position[1]]
                chessboard[list_actual_position[0]][list_actual_position[1]] = '.'
                return chessboard
            elif piece_next_case != '.':
                if piece_next_case.color == self.color or piece_next_case.position == actual_position: #must be free or other color / must move
                    print('error: the bishop cannot do this move')
                else:        #kills
                    piece_next_case.position = ''
                    self.position = list_next_position[1] + str(list_next_position[0])
                    chessboard[list_next_position[0]][list_next_position[1]] = chessboard[list_actual_position[0]][list_actual_position[1]]
                    chessboard[list_actual_position[0]][list_actual_position[1]] = '.'


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
            pass                    # must break the while loop

    def __str__(self):
        return str(self.name)

    def move(self, move_on_chessboard):
        move = convert_to_list(move_on_chessboard)  # convert
        actual_pos = self.position
        alpha_string = "abcdefgh"
        number = 0
        if_exit(move)
        while True:
            for letter in range(8):
                if alpha_string[letter] == actual_pos[0]:
                    number = letter
            if ((int(actual_pos[1]) - move[0]) > 1) | ((int(actual_pos[1]) - move[0]) < -1) | \
                    ((number - move[1]) > 1) | ((number - move[1]) < -1):
                print("Bad value ! Retry !")
                retry = input("Target position : ")
                if_exit(retry)
                move = convert_to_list(verify_position(retry))
            elif move[1] == number & move[0] == int(actual_pos[1]):
                print("It's the same place ! Change the position !")
                retry = input("Target position : ")
                if_exit(retry)
                move = convert_to_list(verify_position(retry))
            elif chessboard[move[0]][alpha_string[number]].color == self.color:
                print("The target position is used by a same color object !")
                retry = input("Target position : ")
                if_exit(retry)
                move = convert_to_list(verify_position(retry))
            else:
                chessboard[move[0]][alpha_string[number]] = chessboard[actual_pos[1]][actual_pos[0]]
                chessboard[actual_pos[1]][actual_pos[0]] = '.'
                chessboard[move[0]][alpha_string[number]].position = str(alpha_string[move[1]]) + str(move[0])
                print("Player x has played ! Next !")
                return 1


# Creation of the pieces instead of creating 32 objects one by one
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
