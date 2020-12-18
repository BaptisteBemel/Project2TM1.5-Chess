# -*- coding: utf8 -*-
import socket
from lib.utility.util import *
from lib.classDir.class_file import pieces, has_played, update_gui_srv, new_player\


# Gets the return of initial_game() which his the right chessboard
chessboard_srv = start()

str_alpha = 'abcdefgh'

# Create a UDP socket for IPv4
srv_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address
srv_s.bind((socket.gethostname(), 12345))
while True:
    # Receive data from the client
    data, addr = srv_s.recvfrom(4096)
    pos_initial_received = data.decode() # att list str
    data, addr = srv_s.recvfrom(4096)
    nxt_pos_received = data.decode()

    pos_initial_received = eval(pos_initial_received)
    # Move the piece that the client played
    chessboard_srv[pos_initial_received[0]][str_alpha[pos_initial_received[1]]].move(nxt_pos_received)
    new_player.who_is_playing = 1
    print(new_player.who_is_playing)
    chessboard = chessboard_srv
    show_chessboard()
    #update_gui_srv()

    while True:
        # If the serveur has played, it sends the data to the client
        if has_played == 'True':
            new_player.who_is_playing = 0
            has_played = 'False'

            pos_initial_tosend = bytes(pos_initial_tosend, 'utf-8')
            nxt_pos_tosend = bytes(nxt_pos_tosend, 'utf-8')


            srv_s.sendto(pos_initial_tosend, addr)
            srv_s.sendto(nxt_pos_tosend, addr)



