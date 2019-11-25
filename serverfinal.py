#!/usr/bin/env python3
#lewis elder
#cmp307
#1803904
#doge financial chat server

#initial imports

import socket
from socket import AF_INET, SOCK_STREAM
from threading import Thread
import sys

def accept_incoming_connections():
    """Sets up handling new clients"""
    while True:
        client, client_address = SERVER.accept() #recieves client name and address
        print("%s:%s has connected." % client_address)
        client.send(bytes("Doge Financial Messaging Service", "utf8"))
        addresses[client] = client_address #adds client address to dictionary 
        Thread(target=handle_client, args=(client,)).start() #thread management


def handle_client(client):  #client socket passed as an argument 
    """Handles client connection"""
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name #creates welcome message with name for client
    client.send(bytes(welcome, "utf8")) #sends message to client
    msg = "%s has joined the chat!" % name #alert that a new client has entered
    broadcast(bytes(msg, "utf8")) #broadcast alert
    clients[client] = name #client name added to dictionary

    while True: #client checking condition (see if people are in)
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ") #send message if not equals {quit}
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close() #close client connection
            del clients[client] #remove client that has left from dictionary
            if len(clients) == 0:
                #close server if there are no clients connected (may be removed in later build, for testing purposes)
                SERVER.close()
                sys.exit(0)
                break
            broadcast(bytes("%s has left the chat." % name, "utf8")) #send message with who has left
            break


def broadcast(msg, prefix=""):  #blank prefix is for client names
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {} #dictionary definitions
addresses = {} #dictionary definitions

#server initialisation code

HOST = ''
PORT = 33002
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket.socket(AF_INET, SOCK_STREAM)
SERVER.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
