# -*- coding: utf-8 -*-
import socket
import threading

def listen_to_server():
    while True:
        data = sor.recv(1024)
        print(data.decode('utf-8'))

server = ('127.0.0.1', 8080)
nick = input('Nick: ')

sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))

sor.sendto((nick+' Connect to server').encode('utf-8'), server) # Серверу - привет :)

potok = threading.Thread(target=listen_to_server)
potok.start()

while True:
    message = input()
    sor.sendto(('['+nick+'] '+message).encode('utf-8'), server)
