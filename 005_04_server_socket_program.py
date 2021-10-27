# socketserver module is also very interesting - might want to take a look at it!
# https://realpython.com/python-sockets/ - very important
import socket

# socket module has the following APIs
# socket()
# bind() S
# listen() S
# accept() S
# connect()
# connect_ex()
# send()
# recv()
# close()

# Another test is to check out if TCP/UDP differences exist - when you make your DO droplet
# Packets can be dropped, packets arrive out of order - check for this!

import socket

host = "127.0.0.1"
port = 8080
byte_steam_length = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()
connection, addr = server_socket.accept()
print(connection, addr)

while True:
    data = connection.recv(byte_steam_length)
    print(data)
    if data == "exit".encode("utf-8"):
        break

server_socket.close()
