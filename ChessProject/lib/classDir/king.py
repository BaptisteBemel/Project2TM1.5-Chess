# -*- coding: utf8 -*-
from lib.classDir.class_file import Piece, change_has_played
from lib.utility.util import *


class King(Piece):
    def __init__(self, color, id_piece):
        super().__init__("K", color, 0, id_piece)

    def is_dead(self):
        """
        It is function use to set the value of the dead on 1 to say 'He is dead'
        """
        if self.dead == 0:
            self.dead = 1                # must break the while loop

    def __str__(self):
        """
        :return: Return a string with the name of the piece
        """
        if self.color == "black":
            return str(self.name)
        else:
            return str(self.name)

    def move(self, move_on_chessboard):
        """
        :param move_on_chessboard: It is where we want to send the pawn on the chessboard
        :return: Return False or True according to the end of the function (if the position is not good == False)
        """
        move = convert_to_list(move_on_chessboard)  # convert
        actual_pos = self.position
        alpha_string = "abcdefgh"
        number = 0
        if_exit(move)
        for letter in range(8):
            if alpha_string[letter] == actual_pos[0]:
                number = letter
        # Verify if the King does not move more than he could
        if ((int(actual_pos[1]) - move[0]) > 1) | ((int(actual_pos[1]) - move[0]) < -1) | \
                ((number - move[1]) > 1) | ((number - move[1]) < -1):
            print("Bad value ! Retry !")
            return False
        # Verify if the position entered is not the same of the actual position of the King
        elif (move[1] == number) & (move[0] == int(actual_pos[1])):
            print("It's the same place ! Change the position !")
            return False
        # Verify if the next position is an object or not
        elif chessboard[move[0]][alpha_string[move[1]]] != ".":
            if chessboard[move[0]][alpha_string[move[1]]].color == self.color:
                print("The target position is used by a same color object !")
                return False
            else:
                if chessboard[move[0]][alpha_string[move[1]]].name == 'K':
                    chessboard[move[0]][alpha_string[move[1]]].is_dead()
                chessboard[move[0]][alpha_string[move[1]]] = chessboard[int(actual_pos[1])][actual_pos[0]]
                chessboard[int(actual_pos[1])][actual_pos[0]] = '.'
                self.position = str(alpha_string[move[1]]) + str(move[0])
                print("Player x has played ! Next !")
                change_has_played()
                return True
        else:
            chessboard[move[0]][alpha_string[move[1]]] = chessboard[int(actual_pos[1])][actual_pos[0]]
            chessboard[int(actual_pos[1])][actual_pos[0]] = '.'
            self.position = str(alpha_string[move[1]]) + str(move[0])
            print("Player x has played ! Next !")
            change_has_played()
            return True