import socket

srv_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv_s.bind((socket.gethostname(), 12345))

msg_server = ""

while True:
    data, addr = srv_s.recvfrom(4096)
    print(str(data))
    msg_server = bytes('UDP serv', 'utf-8')
    srv_s.sendto(msg_server, addr)
