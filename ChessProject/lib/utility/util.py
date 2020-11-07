chess_board = {1: {"a": "T", "b": "C", "c": "F", "d": "K", "e": "Q", "f" : "F", "g": "C", "h": "T"},
               2: {"a": "P", "b": "P", "c": "P", "d": "P", "e": "P", "f" : "P", "g": "P", "h": "P"},
               3: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f" : "x", "g": "x", "h": "x"},
               4: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f" : "x", "g": "x", "h": "x"},
               5: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f" : "x", "g": "x", "h": "x"},
               6: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f" : "x", "g": "x", "h": "x"},
               7: {"a": "P", "b": "P", "c": "P", "d": "P", "e": "P", "f" : "P", "g": "P", "h": "P"},
               8: {"a": "T", "b": "C", "c": "F", "d": "K", "e": "Q", "f" : "F", "g": "C", "h": "T"}}


def show_chess_board():
    for id_in_chess_board in range(1, 9):
        print(str(id_in_chess_board) + " " + chess_board[id_in_chess_board]["a"] + chess_board[id_in_chess_board]["b"] + chess_board[id_in_chess_board]["c"] +
              chess_board[id_in_chess_board]["d"], chess_board[id_in_chess_board]["e"] + chess_board[id_in_chess_board]["f"] +
              chess_board[id_in_chess_board]["g"] + chess_board[id_in_chess_board]["h"] + " " + str(id_in_chess_board))

show_chess_board()