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
    if position == "exit":
        exit()
    elif len(position) == 2:
        if (position[0].isalpha() is False) | (position[1].isnumeric() is False):
            while True:
                retry = input("Retry ! Which object do you want to play ? (use position name like 'd4') ")
                if (len(retry) == 2) & (retry[0].isalpha() is True) & (retry[1].isnumeric() is True):
                    letter_chessboard = "abcdefgh"
                    for letter in range(len(letter_chessboard)):
                        if retry[0] == letter_chessboard[letter]:
                            for number in range(1, 9):
                                if number == int(retry[1]):
                                    return retry
                elif retry == "exit":
                    exit()
        else:
            while True:
                if (len(position) == 2) & (position[0].isalpha() is True) & (position[1].isnumeric() is True):
                    letter_chessboard = "abcdefgh"
                    for letter in range(8):
                        if position[0] == letter_chessboard[letter]:
                            for number in range(1, 9):
                                if number == int(position[1]):
                                    return position
                position = input("Retry ! Which object do you want to play ? (use position name like 'd4') ")
    else:
        verify_position(input("Retry !"))
