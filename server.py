# -*- coding: utf-8 -*-
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 8080))
clients = [] # Массив с адрессам пользователей 
print('Server is started')



while True:
    data, addr = server_socket.recvfrom(1024) # Буфер в байтах
    print(data)
    if addr not in clients:
        clients.append(addr)
    for client in clients:
        if client == addr:
            continue
        server_socket.sendto(data,client)