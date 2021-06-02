## This is the flow of messages on the client side
# message
# turn it into a dictionary - with 'from' and 'payload' - or however you want it
# serialize that json_dict packet to turn it into str
# encode it into utf-8 to turn it into a byte-stream
# encrypt the byte-stream with the public key
# send it over the socket

# The contents of the messages are not seen on WireShark - they are scrambled
# TODO - need Wireshark YouTube tutorials

import socket
import json
import rsa

host = "127.0.0.1"
# host = "159.203.113.242"
port = 8080

try:
    # We load the public key file - we don't try to create it - 010_12 scratches _json for creation
    # Setup your encryption
    publicKey = rsa.PublicKey.load_pkcs1(open("rsa_public_key.pem", 'rb').read(), format='PEM')

    # Program starts
    name = input("What's your name: ")

    # Keep sending messages
    while True:
        message = input(name + ": ")
        if message == 'quit':
            break   # breaking out of the while loop would exit the program, sending exit would quit the server
        packet = {'from': name, 'payload': message}
        #json_packet = json.dumps(packet)

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.send(rsa.encrypt(json.dumps(packet).encode(), publicKey))
        client_socket.close()

except Exception as e:
    print(e.args, "Can't pickup the public key")
