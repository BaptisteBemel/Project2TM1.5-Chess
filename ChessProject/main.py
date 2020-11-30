# -*- coding: utf8 -*-
from lib.utility.util import *
from lib.classDir.class_file import creation_pieces, initial_game, pieces
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
kivy.require('2.0.0')


def start_game():
    position_want_to_play = ""
    who_is_playing = 0
    # Cache use to turn back in the game
    cache = ""
    # Temporary is use to have one game difference with the cache
    temp_cache = chessboard
    while True:
        first_question = input("What do you want to do ? ('play' or 'exit') ")
        if first_question == "play":
            start()
            while True:
                if who_is_playing % 2 == 0:
                    print("Player 1")
                else:
                    print("Player 2")
                show_chessboard()
                play = input("Which object do you want to play ? (use position name like 'd4') ")
                if_exit(play)
                play = is_object(play)
                color = is_good_color(play)
                if (who_is_playing % 2 == 0) & (color == "white"):
                    position_want_to_play = verify_position(play)
                    position_move = verify_position(input("Enter the position where you want to move the object : "))
                    chessboard[int(position_want_to_play[1])][position_want_to_play[0]].move(position_move)
                    cache = temp_cache
                    temp_cache = chessboard
                    who_is_playing += 1
                elif (who_is_playing % 2 == 1) & (color == "black"):
                    position_want_to_play = verify_position(play)
                    position_move = verify_position(input("Enter the position where you want to move the object : "))
                    chessboard[int(position_want_to_play[1])][position_want_to_play[0]].move(position_move)
                    cache = temp_cache
                    temp_cache = chessboard
                    who_is_playing += 1
                else:
                    print("You can not move this color ! Retry !")
                if (pieces["king"][0].dead == 1) | (pieces["king"][1].dead == 1):
                    print("It's the end of this game ! We thank you for playing !")
                    break
        elif (first_question == "exit") | (first_question == "ex"):
            exit()
        else:
            print("Your response is wrong please retry !")


class ChessGame(App):
    def build(self):
        wid = Builder.unload_file("./chess_game.kv")
        return wid


if __name__ == "__main__":
    ChessGame().run()
    # start_game()

