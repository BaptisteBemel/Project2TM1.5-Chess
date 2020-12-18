# -*- coding: utf8 -*-
from lib.classDir.class_file import pieces, Piece, whats_on_case
from lib.utility.util import *


class Pawn(Piece):
    def __init__(self, color, id_piece):
        """
        The number of plays is a id variable use for the 'move' function
        """
        super().__init__("P", color, 0, id_piece)
        self.nb_plays = 0

    def __str__(self):
        """
        :return: Return a string with the name of the piece
        """
        if self.color == "black":
            return str(self.name)
        else:
            return str(self.name)

    def move(self, nxt_position):
        """

        :param nxt_position: The next position is where we want to send the pawn on the chessboard
        :return: Return False or True according to the end of the function (if the position is not good == False)
        """
        if_exit(nxt_position)
        actual_position = convert_to_list(pieces['pawn'][self.id_piece].position)
        list_actual_position = sorted(pieces['pawn'][self.id_piece].position)
        list_actual_position[0] = int(list_actual_position[0])
        list_next_position = sorted(nxt_position)
        list_next_position[0] = int(list_next_position[0])
        piece_next_case = whats_on_case(nxt_position)
        next_position = convert_to_list(nxt_position)
        # deplacement in columns then lines
        move_list = [next_position[0] - actual_position[0], next_position[1] - actual_position[1]]

        if self.color == 'white' and move_list[0] > -1:
            print('error: the pawn cannot move back')
            return False
        elif self.color == 'black' and move_list[0] < 1:
            print('error: the pawn cannot move back')
            return False
        else:
            move_list_abs = [abs(move_list[0]), abs(move_list[1])]
            if len(move_list_abs) != 2:                                    # Wrong move
                print('error: 2 arguments needed')
                return False
            elif move_list_abs[1] > 1 or move_list_abs[0] > 2 or move_list_abs[0] < 1 or move_list_abs[1] < 0:
                print('error: this move is impossible for a pawn')
                return False
            elif move_list_abs[1] == 1:
                # If this kills another piece - no piece of the same color + piece of the other color needed
                if move_list_abs[0] == 1:
                    if chessboard[next_position[0]][list_next_position[1]] == '.':
                        print('error: this move is impossible for a pawn')
                        return False
                    elif piece_next_case.color == self.color:           # if that's the same color
                        print('error: there is already another piece of the same color on this case')
                        return False
                    # Other color: it can kill it, the piece which moves take its position and the other disappears
                    elif piece_next_case.color != self.color:
                        self.position = list_next_position[1] + str(list_next_position[0])
                        piece_next_case.position = ''
                        chessboard[list_next_position[0]][list_next_position[1]] = chessboard[list_actual_position[0]][
                            list_actual_position[1]]
                        chessboard[list_actual_position[0]][list_actual_position[1]] = '.'
                        self.nb_plays = self.nb_plays + 1        # The pawn has played, it won't be its first play again
                        has_played = True
                        return True
                else:
                    print('error: this pawn cannot do this move')
                    return False
            elif move_list_abs[1] == 0:
                if chessboard[list_next_position[0]][list_next_position[1]] != '.':  # Next position must be free
                    print('error: there is already another piece there')
                    return False
                else:
                    if move_list_abs[0] == 2:
                        if self.nb_plays == 0:                      # First time this pawn plays, it can advance 2 cases
                            self.position = list_next_position[1] + str(list_next_position[0])
                            chessboard[list_next_position[0]][list_next_position[1]] = chessboard[
                                list_actual_position[0]][list_actual_position[1]]
                            chessboard[list_actual_position[0]][list_actual_position[1]] = '.'
                            self.nb_plays = self.nb_plays + 1
                            has_played = True
                            return True
                        elif self.nb_plays > 0:
                            print('error: this pawn cannot do this move')
                            return False
                    if move_list_abs[0] == 1:
                        self.position = list_next_position[1] + str(list_next_position[0])
                        chessboard[list_next_position[0]][list_next_position[1]] = chessboard[
                            list_actual_position[0]][list_actual_position[1]]
                        chessboard[list_actual_position[0]][list_actual_position[1]] = '.'
                        self.nb_plays = self.nb_plays + 1
                        has_played = True
                        return True