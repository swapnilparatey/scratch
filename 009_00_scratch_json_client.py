# Since we're using TCP sockets - and if we want multiple clients to connect to a server socket
# we have to relinquish the connection - and then create a new socket and connect again
# connecting to a socket - by a client involves being latched on to the server socket
# and the server probably doesn't have a ton of sockets - or maybe it does - who knows
# servers don't use multiple threads and processors to handle different users and requests anymore
# they use message queues - and asyncio
# but we'll get into details of that later
# for now this will do!

# The contents of the messages are seen on WireShark - COMPLETELY VISIBLE - NOT SECURE

import socket
import json

host = "127.0.0.1"
# host = "159.203.113.242"
port = 8080

name = input("What's your name: ")

while True:
    message = input(name + ": ")
    packet = { 'from': name, 'payload': message}
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(json.dumps(packet).encode("utf-8"))
    client_socket.close()
