# -*- coding: utf8 -*-
chessboard = {1: {"a": "T", "b": "C", "c": "F", "d": "Q", "e": "K", "f": "F", "g": "C", "h": "T"},
              2: {"a": "P", "b": "P", "c": "P", "d": "P", "e": "P", "f": "P", "g": "P", "h": "P"},
              3: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f": "x", "g": "x", "h": "x"},
              4: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f": "x", "g": "x", "h": "x"},
              5: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f": "x", "g": "x", "h": "x"},
              6: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f": "x", "g": "x", "h": "x"},
              7: {"a": "p", "b": "P", "c": "P", "d": "P", "e": "P", "f": "P", "g": "P", "h": "P"},
              8: {"a": "T", "b": "C", "c": "F", "d": "Q", "e": "K", "f": "F", "g": "C", "h": "T"}}


def show_chessboard():
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


def verify_position(position):
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
    alpha_string = "abcdefgh"
    return_list = [int(string[1])]
    for letter in range(8):
        if alpha_string[letter] == string[0]:
            return_list.append(letter)
            return return_list
    return "Error of string !"


def if_exit(string):
    if (string == "exit") | (string == "ex"):
        exit()
    return 1


def if_change_object(string):
    if (string == "change") | (string == "ch"):
        position = input("Change your object you wanted to play : ")
        return position


def is_object(position):
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
    if chessboard[int(pos[1])][pos[0]].color == 'black':
        return "black"
    else:
        return "white"
