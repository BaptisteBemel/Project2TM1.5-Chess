from lib.utility.util import *
import os
import os
import subprocess


ip_addr = "192.168.1.40"


def update_gui_srv():
    from GUI.kv import ChessGame
    is_serv = "True"
    ChessGame(is_serv)


def change_name(name_ip):
    """
    It takes the value of the ip entered in the connection input and modify the right variable

    :param name_ip: is a string which is an address ip
    :return:
    """
    global ip_addr
    ip_addr = name_ip
    os.startfile("client.py")


has_played = 'False'

ip_addr = "xxx.xxx.xxx.xxx"


def change_has_played():
    global has_played
    has_played = True
    has_played = 'True'


def change_name(name_ip):
    """

    :param name_ip: is a string which is a address ip
    :return:
    """
    global ip_addr
    ip_addr = name_ip
    return ip_addr


def call_sub(act_pos, nxt_pos):
    """
    Use to call a subprocess to load the client and send arguments to it

    :param act_pos: It's the actual position of the first 'click' on the chessboard
    :param nxt_pos: It's the actual position of the second 'click' on the chessboard
    """
    subprocess.call(["python", "client.py", bytes(ip_addr, 'utf-8'), bytes(str(act_pos), 'utf-8'),
                     bytes(nxt_pos, 'utf-8')])


class Player:
    def __init__(self, play=0, kind_of_game=0):
        """
        This class is use to define which part of the game it is (solo, client, who should play now,...)

        :param play: Who may play now
        :param kind_of_game: Define if your are a solo player, client or server
        """
        self.who_is_playing = play
        self.kind_of_game = kind_of_game    # 0 == solo, 1 == multi, 2 == connect

    def next_player(self):
        """
        Set the value of who may play now
        """
        if self.who_is_playing == 0:
            self.who_is_playing = 1
        else:
            self.who_is_playing = 0


new_player = Player()

pieces = {'rook': {}, 'bishop': {}, 'pawn': {}, 'king': {}, 'knight': {}, 'queen': {}}


symbol_to_name = {'P': 'pawn', 'R': 'rook', 'B': 'bishop', 'Q': 'queen', 'N': 'knight', 'K': 'king'}


def whats_on_case(pos):
    """

    :param pos: it's an position (example : 'a7')
    :return:
    """
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
        """
        :param name: A string with the little name of the piece
        :param color: There are only two color (black or white)
        :param dead: Define if the piece is dead or not (0 == not dead and 1 == is dead)
        :param id_piece: The id is use in the pieces dictionary
        :param position: The actual position where is place the piece on the chessboard
        """
        self.color = color
        self.name = name
        self.dead = dead
        self.position = position
        self.id_piece = id_piece


# Creation of the pieces instead of creating 32 objects one by one
def creation_pieces():
    from lib.classDir.pawn import Pawn
    from lib.classDir.rook import Rook
    from lib.classDir.bishop import Bishop
    from lib.classDir.queen import Queen
    from lib.classDir.king import King
    from lib.classDir.knight import Knight
    """
    This method is used to create all the object of the chessboard and put them in the pieces dictionary
    """
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


def initial_game(black_or_white="white"):
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
                        pieces[names][id_].position = "d1"
                        chessboard[1]["d"] = pieces[names][id_]
                    else:
                        pieces[names][id_].position = "d8"
                        chessboard[8]["d"] = pieces[names][id_]
                elif names == "queen":
                    if pieces[names][id_].color == "black":
                        pieces[names][id_].position = "e1"
                        chessboard[1]["e"] = pieces[names][id_]
                    else:
                        pieces[names][id_].position = "e8"
                        chessboard[8]["e"] = pieces[names][id_]
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
    return chessboard
