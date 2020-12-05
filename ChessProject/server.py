import socket
from _thread import *
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server = "localhost"
port = 5555


server_ip = socket.gethostbyname(server)


try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

current_id = "0"


def treaded_client(conn):
    global current_id
    conn.send(str.encode(current_id))
    current_id = "1"
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                print("Recieved: " + reply)

        except socket.error as e:
            print(str(e))