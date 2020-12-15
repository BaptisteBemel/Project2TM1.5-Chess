# -*- coding: utf8 -*-
import socket
from lib.utility.util import chessboard
from lib.classDir.class_file import pieces, has_played


srv_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv_s.bind((socket.gethostname(), 12345))


while True:
    data, addr = srv_s.recvfrom(4096)
    chessboard_received = eval(data)
    chessboard = chessboard_received

    data, addr = srv_s.recvfrom(4096)
    isit_true_false = bool(data.decode())

    if isit_true_false == True:
        break

    if pieces["king"][0].dead == 1:
        msg_server = bytes(str(chessboard), 'utf-8')
        true_false = bytes(str(True), 'utf-8')

        srv_s.sendto(msg_server, addr)
        srv_s.sendto(true_false, addr)

    if has_played == True:
        has_played = False

        msg_server = bytes(str(chessboard), "utf-8")
        true_false = bytes(str(False), 'utf-8')
        srv_s.sendto(msg_server, addr)
        srv_s.sendto(true_false, addr)
    print(data)
    '''new_player.who_is_playing = int(data[len(data) - 1])
    temp = ""
    for value in range(len(data) - 1):
        temp += value
    chessboard = temp
    if new_player.who_is_playing == 1:
        change_msg_server(chessboard)'''
    srv_s.sendto(msg_server, addr)
