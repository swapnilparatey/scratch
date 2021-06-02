import socket

host = "127.0.0.1"
port = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:
    message = input("Message to send to server: ")
    client_socket.send(message[:1023].encode("utf-8"))
    if message == "exit":
        break

print("Exiting client ...")
