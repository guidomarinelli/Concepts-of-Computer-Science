"""
Title: Simple Client Server
Author: [Guido Marinelli](https://github.com/GuidoMarinelli/)
Date created: 2021/08/18
Last modified: 2023/06/25
Description: Client script that creates a network connection at a predetermined rendezvous point, and sends the string
             'To infinity ...' to whatever is listening on the other side. It then waits and prints any responses
             it receives.
"""

import socket

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server listening on localhost: 1313
server_address = ('localhost', 1313)
print(f'Connessione a {server_address[0]}:{server_address[1]}')
sock.connect(server_address)
# send request message
message = b"Verso l'infinito..."
print(f'Il client sta inviando "{message.decode()}"')
sock.sendall(message)
# receives response from the server
reply = sock.recv(11)
print(f'Il client ha ricevuto "{reply.decode()}"')

# closes communication with the server
sock.close()
