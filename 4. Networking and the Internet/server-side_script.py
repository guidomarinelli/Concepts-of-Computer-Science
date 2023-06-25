"""
Title: Simple Client Server
Author: [Guido Marinelli](https://github.com/GuidoMarinelli/)
Date created: 2021/08/18
Last modified: 2023/06/25
Description: Server script accompanying the client example.
"""

import socket

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# match the socket to the localhost port: 1313
server_address = ('localhost', 1313)
sock.bind(server_address)
# listens for connections from the client
sock.listen(1)

print('In attesa che un client si connetta')
client, client_port = sock.accept()
print(f'Connesione dal client {client_port[0]}:{client_port[1]}')

# receives request from client
request = client.recv(19)
print(f'Il client ha inviato "{request.decode()}"')
reply = b'E oltre!'
print(f'Il server risponde "{reply.decode()}"')
client.sendall(reply)

# closes the connection with the client
client.close()
