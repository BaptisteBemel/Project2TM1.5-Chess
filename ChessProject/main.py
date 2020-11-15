from lib.utility.util import *
from lib.classDir.class_file import creation_pieces, initial_game

position_want_to_play = ""

if __name__ == "__main__":
    while True:
        first_question = input("What do you want to do ? ('play' or 'exit') ")
        if first_question == "play":
            creation_pieces()
            initial_game()
            print("Welcome to our chess game ! Good luck and you can start the game !")
            print("(You can enter 'exit' anytime you want to quit the game) \n")
            while True:
                show_chessboard()
                play = input("Which object do you want to play ? (use position name like 'd4') ")
                if_exit(play)
                play = is_object(play)
                position_want_to_play = verify_position(play)
                position_move = verify_position(input("Enter the position where you want to move the object : "))
                chessboard[int(position_want_to_play[1])][position_want_to_play[0]].move(position_move)
        elif (first_question == "exit") | (first_question == "ex"):
            exit()
        else:
            print("Your response is wrong please retry !")
