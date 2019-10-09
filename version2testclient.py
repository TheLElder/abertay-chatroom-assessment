#lewis elder
#version 2 testing before initial development
#connection testing as followed last time

#import socket module
import socket

#creating a socket
s = socket.socket()

#define port to connect on
port = 8081

s.connect(('127.0.0.1', port))

print(s.recv(1024))

s.close()
