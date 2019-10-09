#lewis elder
#version 2 testing before initial development
#connection testing as followed last time

#imports for socket module
import socket

#creating a socket
s = socket.socket()
print("done")

#reserving a port on the server for connection locally
port = 8081
#bind port to socekt, ip is not needed as it will be hosted locally
s.bind(('',port))

#listen on socket for connection
s.listen(5)

while True:

        c,addr = s.accept()
        print("Connection recieved from ")
        print(addr)
        
        c.close()

