# -*- coding: utf8 -*-
from lib.utility.util import *
from lib.classDir.class_file import creation_pieces, initial_game, pieces
import kivy
import threading
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty
kivy.require('2.0.0')


list_of_position_chessboard = ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1",
                               "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
                               "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
                               "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
                               "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
                               "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
                               "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
                               "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"]

class game:
    def start_game(self):
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


class MainWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass





class ChessGame(Screen):
    def __init__(self, **kwargs):
        super(ChessGame, self).__init__(**kwargs)
        self.grid = GridLayout()
        self.add_widget(self.grid)
        self.number = 0
        self.pos = [0, 0]
        self.sth_on_chessboard = False
        self.text_label = "Choose an object"
        self.grid.cols = 8
        self.grid.rows = 8
        self.grid.padding = 100
        self.grid.size = 600, 600
        self.grid.id = "gri"
        max_eight = 0
        start()
        for i in range(len(list_of_position_chessboard)):
            btn = ""
            if max_eight < 8:
                if i % 2 == 0:
                    btn = Button(background_color=(0.95, 0.8, 0.5, 1), background_normal="")
                    self.grid.add_widget(btn)
                else:
                    btn = Button(background_normal="")
                    self.grid.add_widget(btn)
                max_eight += 1
                btn.id = list_of_position_chessboard[i]
                btn.bind(on_press=self.move)
                btn.background_normal = ""
            else:
                if i % 2 == 0:
                    btn = Button(background_normal="")
                    self.grid.add_widget(btn)
                else:
                    btn = Button(background_color=(0.95, 0.8, 0.5, 1), background_normal="")
                    self.grid.add_widget(btn)
                if max_eight == 15:
                    max_eight = -1
                max_eight += 1
                btn.id = list_of_position_chessboard[i]
                btn.bind(on_press=self.move)
                btn.background_normal = ""
                # btn.bind(on_release=self.change_text)
        self.add_pieces_on_chessboard()

    def add_pieces_on_chessboard(self):
        for i in self.grid.children:
            if self.sth_on_chessboard is False:
                if i.id == "a2" or i.id == "b2" or i.id == "b2" or i.id == "c2" or i.id == "d2" or i.id == "e2" or \
                        i.id == "f2" or i.id == "g2" or i.id == "h2":
                    i.background_normal = "./img/black_pawn.png"
                elif i.id == "a7" or i.id == "b7" or i.id == "b7" or i.id == "c7" or i.id == "d7" or i.id == "e7" or \
                        i.id == "f7" or i.id == "g7" or i.id == "h7":
                    i.background_normal = "./img/white_pawn.png"
                elif i.id == "a1" or i.id == "h1":
                    i.background_normal = "./img/black_rook.png"
                elif i.id == "a8" or i.id == "h8":
                    i.background_normal = "./img/white_rook.png"
                elif i.id == "b1" or i.id == "g1":
                    i.background_normal = "./img/black_knight.png"
                elif i.id == "b8" or i.id == "g8":
                    i.background_normal = "./img/white_knight.png"
                elif i.id == "c1" or i.id == "f1":
                    i.background_normal = "./img/black_bishop.png"
                elif i.id == "c8" or i.id == "f8":
                    i.background_normal = "./img/white_bishop.png"
                elif i.id == "d1":
                    i.background_normal = "./img/black_king.png"
                elif i.id == "d8":
                    i.background_normal = "./img/white_king.png"
                elif i.id == "e1":
                    i.background_normal = "./img/black_queen.png"
                elif i.id == "e8":
                    i.background_normal = "./img/white_queen.png"
                if i.id == "a1":
                    self.sth_on_chessboard = True
            if self.sth_on_chessboard is True:
                pass

    def move(self, button):
        letter = "abcdefgh"
        if self.number == 0:
            self.pos = convert_to_list(button.id)
            self.number += 1
            if chessboard[self.pos[0]][letter[self.pos[1]]] == ".":
                self.number -= 1
                print("This value is wrong because it's not an object's position !")
                self.children[1].text = "This value is wrong because it's not an object's position !"
            else:
                self.children[1].text = "Choose the position where you want to put your piece !"
        elif self.number == 1:
            if chessboard[self.pos[0]][letter[self.pos[1]]].move(button.id) is True:
                self.number = 0
                show_chessboard()
                self.children[1].text = "Choose the object you want to move"
            else:
                print("This value is wrong because it's not a correct position !")
                self.children[1].text = "This value is wrong because it's not a correct position !"

    def change_piece_to_play(self):
        self.number = 0


class ChessApp(App):
    def build(self):
        Builder.load_file("chess.kv")
        ChessGame()


if __name__ == "__main__":
    ChessApp().run()
