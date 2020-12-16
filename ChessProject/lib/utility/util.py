# -*- coding: utf8 -*-
chessboard = {1: {"a": "T", "b": "C", "c": "F", "d": "K", "e": "Q", "f": "F", "g": "C", "h": "T"},
              2: {"a": "P", "b": "P", "c": "P", "d": "P", "e": "P", "f": "P", "g": "P", "h": "P"},
              3: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f": "x", "g": "x", "h": "x"},
              4: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f": "x", "g": "x", "h": "x"},
              5: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f": "x", "g": "x", "h": "x"},
              6: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f": "x", "g": "x", "h": "x"},
              7: {"a": "p", "b": "P", "c": "P", "d": "P", "e": "P", "f": "P", "g": "P", "h": "P"},
              8: {"a": "T", "b": "C", "c": "F", "d": "K", "e": "Q", "f": "F", "g": "C", "h": "T"}}


def show_chessboard():
    """
    This show the chessboard into the correct form of it in the console
    """
    stri = "  A B C D E F G H  \n"
    for id_in_chessboard in range(1, 9):
        stri += str(id_in_chessboard) + " " + str(chessboard[id_in_chessboard]["a"]) + " " + \
              str(chessboard[id_in_chessboard]["b"]) + " " + \
              str(chessboard[id_in_chessboard]["c"]) + " " + str(chessboard[id_in_chessboard]["d"]) + " " + \
              str(chessboard[id_in_chessboard]["e"]) + " " + str(chessboard[id_in_chessboard]["f"]) + " " + \
              str(chessboard[id_in_chessboard]["g"]) + " " + str(chessboard[id_in_chessboard]["h"]) + " " + \
              str(id_in_chessboard) + "\n"
    stri += "  A B C D E F G H  \n"
    print(stri)


def start():
    """
    Here, we start the initialisation with the creation of objects (pawn, rook,...) and put them on their correct place
    on the chessboard (console)
    """
    from lib.classDir.class_file import creation_pieces, initial_game
    creation_pieces()
    initial_game()
    print("Welcome to our chess game ! Good luck and you can start the game !")
    print("(You can enter 'exit' anytime you want to quit the game) \n")


def verify_position(position):
    """
    We find if the string entered is a correct form for the methods we will call later

    :param position: it's a string verify in this method
    :return: it return the correct form of the string
    """
    while True:
        if_exit(position)
        if len(position) == 2:
            if (position[0].isalpha() is False) | (position[1].isnumeric() is False):
                while True:
                    retry = input("Retry ! (use position name like 'd4') ")
                    if (len(retry) == 2) & (retry[0].isalpha() is True) & (retry[1].isnumeric() is True):
                        letter_chessboard = "abcdefgh"
                        for letter in range(len(letter_chessboard)):
                            if retry[0] == letter_chessboard[letter]:
                                for number in range(1, 9):
                                    if number == int(retry[1]):
                                        return retry
                    if_exit(retry)
            else:
                while True:
                    if (len(position) == 2) & (position[0].isalpha() is True) & (position[1].isnumeric() is True):
                        letter_chessboard = "abcdefgh"
                        for letter in range(8):
                            if position[0] == letter_chessboard[letter]:
                                for number in range(1, 9):
                                    if number == int(position[1]):
                                        return position
                    position = input("Retry ! (use position name like 'd4') ")
        else:
            position = input("Retry ! ")


def convert_to_list(string):
    """
    It convert the string of the position to a list of number which represent the letter and the number

    :param string: the string is the position
    :return: It return the list
    """
    alpha_string = "abcdefgh"
    return_list = [int(string[1])]
    for letter in range(8):
        if alpha_string[letter] == string[0]:
            return_list.append(letter)
            return return_list
    return "Error of string !"


def if_exit(string):
    """
    If the string is equal to 'exit' it quit
    """
    if (string == "exit") | (string == "ex"):
        exit()
    return 1


def if_change_object(string):
    """
    If the string is equal to 'change' or 'ch' it change the piece we want to play
    """
    if (string == "change") | (string == "ch"):
        position = input("Change your object you wanted to play : ")
        return position


def is_object(position):
    """
    Verify if the position equal the position of an object. If True, it return the position
    """
    position = verify_position(position)
    if position == "":
        while True:
            position = verify_position(position)
            if position == "":
                pass
            elif chessboard[int(position[1])][position[0]] != ".":
                return position
            position = input("This position is not an object, please change : ")
    elif chessboard[int(position[1])][position[0]] == ".":
        while True:
            position = input("This position is not an object, please change : ")
            position = verify_position(position)
            if chessboard[int(position[1])][position[0]] != ".":
                return position
    return position


def is_good_color(pos):
    """
    Find if the color of the target is black or white
    """
    if chessboard[int(pos[1])][pos[0]].color == 'black':
        return "black"
    else:
        return "white"
