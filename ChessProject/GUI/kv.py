# -*- coding: utf8 -*-
from lib.utility.util import *
from lib.classDir.class_file import Player
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
from kivy.properties import ObjectProperty
import os

list_of_position_chessboard = ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1",
                               "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
                               "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
                               "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
                               "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
                               "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
                               "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
                               "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"]

new_player = Player()
ip_address = "192.168.1.40"

has_played = False


def change_has_played():
    has_played = True


def change_name(name_ip):
    """

    :param name_ip: is a string which is a address ip
    :return:
    """
    ip_address = name_ip
    os.startfile("client.py")


class MainWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class SoloOrMulti(Screen):
    def run_server(self):
        os.startfile("server.py")
        new_player.kind_of_game = 1
        start()
        show_chessboard()

    def solo_game(self):
        start()
        show_chessboard()


class ConnectWindow(Screen):
    def connect_to_server(self):
        pass
        if len(self.children[0].children[1].text) < 7 or len(self.children[0].children[1].text) > 15:
            print("Bad Value !")
        elif self.children[0].children[1].text.split(".") is False:
            print("It is not an ip address !")
        else:
            self.manager.current = "game"
            new_player.who = 1
            new_player.kind_of_game = 2
            start()
            change_name(self.children[0].children[1].text)


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
        self.grid.id = "grid"
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
        """
        This function add pieces on the interface of the chessboard (Kivy)
        :return:
        """
        for btn in self.grid.children:
            if btn.id == "a2" or btn.id == "b2" or btn.id == "b2" or btn.id == "c2" or btn.id == "d2" or \
                    btn.id == "e2" or btn.id == "f2" or btn.id == "g2" or btn.id == "h2":
                btn.background_normal = "./img/black_pawn.png"
            elif btn.id == "a7" or btn.id == "b7" or btn.id == "b7" or btn.id == "c7" or btn.id == "d7" or \
                    btn.id == "e7" or btn.id == "f7" or btn.id == "g7" or btn.id == "h7":
                btn.background_normal = "./img/white_pawn.png"
            elif btn.id == "a1" or btn.id == "h1":
                btn.background_normal = "./img/black_rook.png"
            elif btn.id == "a8" or btn.id == "h8":
                btn.background_normal = "./img/white_rook.png"
            elif btn.id == "b1" or btn.id == "g1":
                btn.background_normal = "./img/black_knight.png"
            elif btn.id == "b8" or btn.id == "g8":
                btn.background_normal = "./img/white_knight.png"
            elif btn.id == "c1" or btn.id == "f1":
                btn.background_normal = "./img/black_bishop.png"
            elif btn.id == "c8" or btn.id == "f8":
                btn.background_normal = "./img/white_bishop.png"
            elif btn.id == "d1":
                btn.background_normal = "./img/black_king.png"
            elif btn.id == "d8":
                btn.background_normal = "./img/white_king.png"
            elif btn.id == "e1":
                btn.background_normal = "./img/black_queen.png"
            elif btn.id == "e8":
                btn.background_normal = "./img/white_queen.png"

    def update_chessboard_GUI(self):
        child = self.children[3].children
        for key_chessboard in list_of_position_chessboard:
            if chessboard[int(key_chessboard[1])][key_chessboard[0]] == ".":
                for btn in child:
                    if btn.id == key_chessboard:
                        btn.background_normal = ""
            elif chessboard[int(key_chessboard[1])][key_chessboard[0]].name == "R":
                for btn in child:
                    if btn.id == key_chessboard:
                        if chessboard[int(key_chessboard[1])][key_chessboard[0]].color == "black":
                            btn.background_normal = "./img/black_rook.png"
                        else:
                            btn.background_normal = "./img/white_rook.png"
            elif chessboard[int(key_chessboard[1])][key_chessboard[0]].name == "B":
                for btn in child:
                    if btn.id == key_chessboard:
                        if chessboard[int(key_chessboard[1])][key_chessboard[0]].color == "black":
                            btn.background_normal = "./img/black_bishop.png"
                        else:
                            btn.background_normal = "./img/white_bishop.png"
            elif chessboard[int(key_chessboard[1])][key_chessboard[0]].name == "P":
                for btn in child:
                    if btn.id == key_chessboard:
                        if chessboard[int(key_chessboard[1])][key_chessboard[0]].color == "black":
                            btn.background_normal = "./img/black_pawn.png"
                        else:
                            btn.background_normal = "./img/white_pawn.png"
            elif chessboard[int(key_chessboard[1])][key_chessboard[0]].name == "N":
                for btn in child:
                    if btn.id == key_chessboard:
                        if chessboard[int(key_chessboard[1])][key_chessboard[0]].color == "black":
                            btn.background_normal = "./img/black_knight.png"
                        else:
                            btn.background_normal = "./img/white_knight.png"
            elif chessboard[int(key_chessboard[1])][key_chessboard[0]].name == "Q":
                for btn in child:
                    if btn.id == key_chessboard:
                        if chessboard[int(key_chessboard[1])][key_chessboard[0]].color == "black":
                            btn.background_normal = "./img/black_queen.png"
                        else:
                            btn.background_normal = "./img/white_queen.png"
            elif chessboard[int(key_chessboard[1])][key_chessboard[0]].name == "K":
                for btn in child:
                    if btn.id == key_chessboard:
                        if chessboard[int(key_chessboard[1])][key_chessboard[0]].color == "black":
                            btn.background_normal = "./img/black_king.png"
                        else:
                            btn.background_normal = "./img/white_king.png"

    def move(self, button):
        letter = "abcdefgh"
        if self.number == 0:
            self.pos = convert_to_list(button.id)
            self.number += 1
            if chessboard[self.pos[0]][letter[self.pos[1]]] == ".":
                self.number -= 1
                print("This value is wrong because it's not an object's position !")
                self.children[2].text = "This value is wrong because it's not an object's position !"
            elif (chessboard[self.pos[0]][letter[self.pos[1]]].color == "black" and new_player.who_is_playing == 0) or \
                    (chessboard[self.pos[0]][letter[self.pos[1]]].color == "white" and new_player.who_is_playing == 1):
                self.number -= 1
                print("Not your turn !")
                self.children[2].text = "Not your turn !"
            elif (chessboard[self.pos[0]][letter[self.pos[1]]].color == "black" and new_player.kind_of_game == 1) or \
                    (chessboard[self.pos[0]][letter[self.pos[1]]].color == "white" and new_player.kind_of_game == 2):
                self.number -= 1
                print("This value is wrong because it's the bad color !")
                self.children[2].text = "This value is wrong because it's the bad color !"
            else:
                self.children[2].text = "Choose the position where you want to put your piece !"
        elif self.number == 1:
            if chessboard[self.pos[0]][letter[self.pos[1]]].move(button.id) is True:
                self.number = 0
                show_chessboard()
                self.update_chessboard_GUI()
                change_has_played()
                self.children[2].text = "Choose the object you want to move"
            else:
                print("This value is wrong because it's not a correct position !")
                self.children[2].text = "This value is wrong because it's not a correct position !"

    def change_piece_to_play(self):
        self.number = 0

    def reset_game(self):
        start()
        self.update_chessboard_GUI()
        new_player.who_is_playing = 0


class ChessApp(App):
    def build(self):
        Builder.load_file("./GUI/chess.kv")
        ChessGame()
