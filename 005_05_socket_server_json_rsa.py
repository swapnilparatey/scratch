## IMPORTANT - you were debugging this flow for a while
# Use these steps in the server
# receive your encrypted message from the socket connection
# decrypt the message with the private key - that's how RSA asymmetric encryption works - sender uses public key to send
# decode from byte-stream to string - explicitly specify utf-8 in both - or just default
# now you have your json serialized packet - run loads on it
# now you have your json dictionary - use keys to extract relevant values

# The contents of the messages are not seen on WireShark - they are scrambled
# TODO - need Wireshark YouTube tutorials

import socket
import json
import rsa


host = "127.0.0.1"
#host = "159.203.113.242" - that worked
port = 8080
byte_steam_length = 500 # This depends on nbits - see the encryption nbits why - because the message can't be longer


try:
    privateKey = rsa.PrivateKey.load_pkcs1(open("rsa_private_key.pem",'rb').read(),format='PEM')
    # if your privateKey isn't made - use 010_02 to make your private key
    print("Private key loaded - creating socket - will be ready to receive messages")

    # create your socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    while True:
        connection, addr = server_socket.accept()
        json_dict_data = json.loads(rsa.decrypt(connection.recv(byte_steam_length), privateKey).decode())
        print(json_dict_data['from'], "said:", json_dict_data['payload'])
        if json_dict_data['payload'] == 'exit':
            server_socket.close()
            exit(0)

except Exception as e:
    print(e.args, "We need to stop the program here")
    exit(0)

