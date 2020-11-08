chessboard = {1: {"a": "T", "b": "C", "c": "F", "d": "K", "e": "Q", "f": "F", "g": "C", "h": "T"},
               2: {"a": "P", "b": "P", "c": "P", "d": "P", "e": "P", "f": "P", "g": "P", "h": "P"},
               3: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f": "x", "g": "x", "h": "x"},
               4: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f": "x", "g": "x", "h": "x"},
               5: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f": "x", "g": "x", "h": "x"},
               6: {"a": "x", "b": "x", "c": "x", "d": "x", "e": "x", "f": "x", "g": "x", "h": "x"},
               7: {"a": "P", "b": "P", "c": "P", "d": "P", "e": "P", "f": "P", "g": "P", "h": "P"},
               8: {"a": "T", "b": "C", "c": "F", "d": "K", "e": "Q", "f": "F", "g": "C", "h": "T"}}



def show_chessboard():
    print("  abcdefgh  ")
    for id_in_chessboard in range(1, 9):
        print(str(id_in_chessboard) + " " + chessboard[id_in_chessboard]["a"] + chessboard[id_in_chessboard]["b"] +
              chessboard[id_in_chessboard]["c"] + chessboard[id_in_chessboard]["d"] +
              chessboard[id_in_chessboard]["e"] + chessboard[id_in_chessboard]["f"] +
              chessboard[id_in_chessboard]["g"] + chessboard[id_in_chessboard]["h"] + " " + str(id_in_chessboard))
    print("  abcdefgh  ")
