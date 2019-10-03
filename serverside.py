import socket
from socket import AF_INET, SOCK_STREAM
import select
import sys
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP = '127.0.0.1'
port = 8081

clientslist = []

def clientthread(con, addr):

    con.send ("welcome")

    while True:
        try:
            message = con.recv(2048)
            if message:

                """prints recieved message"""

                print ("<" + addr[0] + "> " + message)

                messagesend = ("<" + addr[0] + "> " + message)
                broadcast(messagesend, con)

            else:

                remove(con)
        except:
            continue

def broadcast(message, con):

    for clients in clientslist:
        if clients != con:
            try:
                clients.send(message)
            except:
                clients.close()

                remove(clients)

def remove(con):
    if conn in clientslist:
        clientslist.remove(conn)

if __name__ == "__main__":

    con, addr = server.accept()

    clientslist.append(con)

    print (addr[0] + " joined")

    start_thread(clientthread,(con,add))

con.close()
server.close()
