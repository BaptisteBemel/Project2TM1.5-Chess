# -*- coding: utf8 -*-
import socket
from lib.utility.util import chessboard
from GUI.kv import new_player

srv_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv_s.bind(('127.0.0.1', 12345)) #socket.gethostname()

msg_server = bytes("", "utf-8")


def change_msg_server(msg):
    msg_server = bytes(str(msg) + str(new_player.who_is_playing), "utf-8")
    srv_s.sendto(msg_server, addr)


while True:
    data, addr = srv_s.recvfrom(4096)
    new_player.who_is_playing = int(data[len(data) - 1])
    temp = ""
    for value in range(len(data) - 1):
        temp += value
    chessboard = temp
    if new_player.who_is_playing == 1:
        change_msg_server(chessboard)
    srv_s.sendto(msg_server, addr)
