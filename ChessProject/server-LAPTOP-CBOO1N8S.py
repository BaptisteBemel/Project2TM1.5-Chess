# -*- coding: utf8 -*-
import socket
from lib.utility.util import chessboard
# from GUI.kv import new_player

srv_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv_s.bind((socket.gethostname(), 12345))
msg_server = bytes(str(chessboard), "utf-8")


while True:
    data, addr = srv_s.recvfrom(4096)
    print("[Data Received]")
    data = eval(data)
    if data != chessboard:
        chessboard = data
    print(data)

    srv_s.sendto(msg_server, addr)
    print("[Data send]")


