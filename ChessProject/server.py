# -*- coding: utf8 -*-
import socket
from lib.utility.util import *
from lib.classDir.class_file import pieces, has_played, update_gui_srv

chessboard_srv = start()

str_alpha = 'abcdefgh'

srv_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv_s.bind((socket.gethostname(), 12345))
while True:

    data, addr = srv_s.recvfrom(4096)
    pos_initial_received = data.decode() # att list str
    data, addr = srv_s.recvfrom(4096)
    nxt_pos_received = data.decode()

    pos_initial_received = eval(pos_initial_received)
    chessboard_srv[pos_initial_received[0]][str_alpha[pos_initial_received[1]]].move(nxt_pos_received)



    while True:
        update_gui_srv()
        if has_played == 'True':
            has_played = 'False'

            pos_initial_tosend = bytes(pos_initial, 'utf-8')
            nxt_pos_tosend = bytes(nxt_pos, 'utf-8')

            srv_s.sendto(pos_initial_tosend, addr)
            srv_s.sendto(nxt_pos_tosend, addr)



















'''
while True:
    # data, addr = srv_s.recvfrom(4096)
    srv_s.settimeout(1)
    try:
        recvpack, payload = srv_s.recvfrom(4096)
    except socket.timeout:
        recvpack = None
    if recvpack is not None:
        print(recvpack)
        data, addr = srv_s.recvfrom(4096)
        print(data.decode())
        data, addr = srv_s.recvfrom(4096)

        chessboard_received = eval(data)
        print(chessboard == chessboard_received)
        chessboard = chessboard_received


        data, addr = srv_s.recvfrom(4096)
        isit_true_false = bool(data.decode())

        if isit_true_false == True:
            break


<<<<<<< HEAD

    if new_play.has_played == True:
=======
    if has_played == True:
>>>>>>> 5b3f4ccdd6f22c6203895f7e22ee57b96d62019f
        has_played = False

        msg_server = bytes(str(chessboard), "utf-8")
        true_false = bytes(str(False), 'utf-8')
        srv_s.sendto(msg_server, addr)
        srv_s.sendto(true_false, addr)
'''
