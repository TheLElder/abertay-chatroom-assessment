import socket
from socket import AF_INET, SOCK_STREAM
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockets = []

IP = '127.0.0.1'
port = 8081

try:
    server.bind((IP, port))
    print("passed")
except:
    print("failed")

while True:

    sockets.append(server)

    read_socket, write_socket, error_socket = select.select(sockets,[],[])

    for sock in read_socket:
        if sock == server:
            message = sock.recv(2048)
            print(message)
        else:
            message = sys.stdin.readLine()
            server.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
            
server.close()
