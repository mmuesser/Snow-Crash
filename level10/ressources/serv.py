#! /usr/bin/python3

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("192.168.56.101", 6969)
sock.bind(server_address)
printf("starting server on %s port %s" % server_address)
sock.listen(1)

while True :
    print("waiting for connection")
    connection, client_address = sock.accept()
    print("connection from" % client_address)
    while True :
        data = connection.recv(64)
        print('received "%s"' % data)
        if len(data) < 1:
            connection.close()
            break
    break
