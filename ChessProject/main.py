from lib.utility.util import *
from lib.classDir.class_file import *

position_want_to_play = ""

if __name__ == "__main__":
    first_question = input("What do you want to do ? ('play' or 'exit') ")
    print(first_question)
    if first_question == "play":
        creation_pieces()
        initial_game()
        print("Welcome to our chess game ! Good luck and you can start the game !")
        while True:
            show_chessboard()
            play = input("Which object do you want to play ? (use position name like 'd4') ")
            if play == "exit":
                exit()
            else:
                position_want_to_play = verify_position(play)
    elif first_question == "exit":
        exit()
    else:
        print("Your response is wrong please retry !")
