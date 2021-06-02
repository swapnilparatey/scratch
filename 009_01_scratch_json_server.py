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

# [TODO] No way in hell i'm doing to study about select right now - that's depressing
# The contents of the messages are seen on WireShark - COMPLETELY VISIBLE - NOT SECURE


import socket
import json

host = "127.0.0.1"
#host = "159.203.113.242" - that worked
port = 8080
byte_steam_length = 1024


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

while True:
    connection, addr = server_socket.accept()
    print(connection, addr)
    json_dict_data = json.loads(connection.recv(byte_steam_length))
    print(json_dict_data['from'], " said :", json_dict_data['payload'])
    if json_dict_data['payload'] == 'exit':
        break

server_socket.close()