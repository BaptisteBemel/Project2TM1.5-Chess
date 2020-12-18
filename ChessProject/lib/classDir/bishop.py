# -*- coding: utf8 -*-
from lib.classDir.class_file import pieces, Piece, whats_on_case
from lib.utility.util import *


class Bishop(Piece):
    def __init__(self, color, id_piece):
        super().__init__("B", color, 0, id_piece)

    def move(self, nxt_position):
        """
        :param nxt_position: The next position is where we want to send the pawn on the chessboard
        :return: Return False or True according to the end of the function (if the position is not good == False)
        """
        if_exit(nxt_position)
        actual_position = convert_to_list(pieces['bishop'][self.id_piece].position)
        list_actual_position = sorted(pieces['bishop'][self.id_piece].position)
        list_actual_position[0] = int(list_actual_position[0])
        list_next_position = sorted(nxt_position)
        list_next_position[0] = int(list_next_position[0])
        piece_next_case = whats_on_case(nxt_position)
        next_position = convert_to_list(nxt_position)
        move_list = [next_position[0] - actual_position[0], next_position[1] - actual_position[1]]
        move_list_abs = [abs(move_list[0]), abs(move_list[1])]
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

        if move_list_abs[0] != move_list_abs[1]:    # must be a diagonal
            print('error: the bishop cannot do this move')
            return False
        elif sth_on_way:
            print('error: something is on the way')
            return False
        else:
            if piece_next_case == '.':
                self.position = list_next_position[1] + str(list_next_position[0])
                chessboard[list_next_position[0]][list_next_position[1]] = chessboard[list_actual_position[0]][
                    list_actual_position[1]]
                chessboard[list_actual_position[0]][list_actual_position[1]] = '.'
                return True
            elif piece_next_case != '.':
                # must be free or other color / must move
                if piece_next_case.color == self.color or convert_to_list(piece_next_case.position) == actual_position:
                    print('error: the bishop cannot do this move')
                    return False
                else:        # kills
                    piece_next_case.position = ''
                    self.position = list_next_position[1] + str(list_next_position[0])
                    chessboard[list_next_position[0]][list_next_position[1]] = chessboard[list_actual_position[0]][
                        list_actual_position[1]]
                    chessboard[list_actual_position[0]][list_actual_position[1]] = '.'
                    return True

    def __str__(self):
        """
        :return: Return a string with the name of the piece
        """
        if self.color == "black":
            return str(self.name)
        else:
            return str(self.name)