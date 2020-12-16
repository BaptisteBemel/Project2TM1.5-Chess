# -*- coding: utf8 -*-
import socket
from lib.utility.util import chessboard
from lib.classDir.class_file import pieces, has_played


srv_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv_s.bind((socket.gethostname(), 12345))


while True:
    data, addr = srv_s.recvfrom(4096)
    print(data.decode())
    srv_s.settimeout(1)
    try:
        recvpack, payload = srv_s.recvfrom(4096)
    except socket.timeout:
        recvpack = None
    if recvpack is not None:
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



    if new_play.has_played == True:
        has_played = False

        msg_server = bytes(str(chessboard), "utf-8")
        true_false = bytes(str(False), 'utf-8')
        srv_s.sendto(msg_server, addr)
        srv_s.sendto(true_false, addr)

