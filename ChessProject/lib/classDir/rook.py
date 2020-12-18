# -*- coding: utf8 -*-
from lib.classDir.class_file import Piece, change_has_played
from lib.utility.util import *


class Rook(Piece):
    def __init__(self, color, id_piece):
        super().__init__("R", color, 0, id_piece)

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
        move = convert_to_list(move_on_chessboard)  # Convert the string (example 'h8') in list '[8, 7]
        actual_position = self.position
        alpha_string = "abcdefgh"
        if_exit(move)
        max_value = 0
        min_value = 0
        is_good_way = True
        # Verify if it's a good translation for the rook
        if ((move[0] != int(actual_position[1])) & (alpha_string[move[1]] != actual_position[0])) | \
                ((move[0] == int(actual_position[1])) & (alpha_string[move[1]] == actual_position[0])):
            print("The value is the same of the position of the object or your rook can not move the abscissa " + \
                  "and the ordinate at the same time")
            return False
        # Verify if the object is moving on the ordonate
        elif (move[0] != int(actual_position[1])) & (alpha_string[move[1]] == actual_position[0]):
            is_good_way = True
            if move[0] > int(actual_position[1]):
                max_value = move[0]
                min_value = int(actual_position[1]) + 1
            else:
                max_value = int(actual_position[1])
                min_value = move[0] + 1
            if min_value != max_value:
                # Verify if there is something on the way of the rook
                for ordonate in range(min_value, max_value):
                    if chessboard[ordonate][actual_position[0]] != ".":
                        is_good_way = False
                        print("There is an object on the way of the rook !")
                        retry = input("Choose an another position : ")
                        if_exit(retry)
                        move = convert_to_list(verify_position(retry))
                        break
            # Verify if the position where the object is moving is used by an other object with an opposite color
            if (chessboard[move[0]][alpha_string[move[1]]] != ".") & (is_good_way is True):
                if chessboard[move[0]][alpha_string[move[1]]].color == self.color:
                    print("The color of the object on the position entered is the same")
                    return False
                else:
                    chessboard[move[0]][alpha_string[move[1]]] = chessboard[int(actual_position[1])][
                        actual_position[0]]
                    chessboard[int(actual_position[1])][actual_position[0]] = "."
                    self.position = str(alpha_string[move[1]]) + str(move[0])
                    change_has_played()
                    return True
            elif is_good_way is True:
                chessboard[move[0]][alpha_string[move[1]]] = chessboard[int(actual_position[1])][actual_position[0]]
                chessboard[int(actual_position[1])][actual_position[0]] = "."
                self.position = str(alpha_string[move[1]]) + str(move[0])
                change_has_played()
                return True
        # Verify if the object is moving on the abscissa
        elif (move[0] == int(actual_position[1])) & (alpha_string[move[1]] != actual_position[0]):
            is_good_way = True
            number_actual = 0
            number = 0
            for letter in range(8):
                if alpha_string[letter] == alpha_string[move[1]]:
                    number = letter
                    break
            for letter in range(8):
                if alpha_string[letter] == actual_position[0]:
                    number_actual = letter
                    break
            if number > number_actual:
                max_value = number
                min_value = number_actual + 1
            elif (number_actual - number) > 1:
                max_value = number_actual
                min_value = number + 1
            if min_value != max_value:
                # Verify if there is something on the way of the rook
                for abscissa in range(min_value, max_value):
                    if chessboard[move[0]][alpha_string[abscissa]] != ".":
                        is_good_way = False
                        print("There is an object on the way of the rook !")
                        break
            # Verify if the position where the object is moving is used by an other object with an opposite color
            if (chessboard[move[0]][alpha_string[move[1]]] != ".") & (is_good_way is True):
                if chessboard[move[0]][alpha_string[move[1]]].color == self.color:
                    print("The color of the object on the position entered is the same")
                    return False
                else:
                    if chessboard[move[0]][alpha_string[move[1]]].name == 'K':
                        chessboard[move[0]][alpha_string[move[1]]].is_dead()
                    chessboard[move[0]][alpha_string[move[1]]] = chessboard[int(actual_position[1])][
                        actual_position[0]]
                    chessboard[int(actual_position[1])][actual_position[0]] = "."
                    self.position = str(alpha_string[move[1]]) + str(move[0])
                    change_has_played()
                    return True
            elif is_good_way is True:
                chessboard[move[0]][alpha_string[move[1]]] = chessboard[int(actual_position[1])][actual_position[0]]
                chessboard[int(actual_position[1])][actual_position[0]] = "."
                self.position = str(alpha_string[move[1]]) + str(move[0])
                change_has_played()
                return True