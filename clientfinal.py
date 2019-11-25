#!/usr/bin/env python3
#lewis elder
#cmp307
#1803904
#doge financial chat client 

#initial imports

import socket
from socket import AF_INET, SOCK_STREAM
from threading import Thread
from tkinter import *

firstclick = True

def on_entry_click(event):
    """function call for first click"""        
    global firstclick

    if firstclick: #firstclick if condition 
        firstclick = False
        entry_field.delete(0, "end") #deletes text in typing box when clicked 


def receive():
    """Receiving messages."""
    #while loop to continously recieve messages
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8") #format text into utf8
            msg_list.insert(END, msg)
        except OSError:  #basic error checking(for client leaving or disconnection)
            break


def send(event=None):  #event passing using binders
    """Sending messages."""
    msg = my_msg.get()
    my_msg.set("")  #clears message field
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        root.quit()


def on_closing(event=None): #event passing using binders
    """Leaving message as client leaves"""
    my_msg.set("{quit}")
    send()

#THe following is the code for tkinter

root = Tk()
root.title("Doge Financial Messaging Service")

#frame for the chat window

messages_frame = Frame(root)
my_msg = StringVar()  #For sending messages
my_msg.set("Type your messages here.")
scrollbar = Scrollbar(messages_frame)  #Scrollbar for older messages

#The following is the box area where messages will be displayed in tkinter

msg_list = Listbox(messages_frame, height=25, width=60, yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()
messages_frame.pack()

#Code for sending messages format in tkinter

text_field = Entry(root, width=40, textvariable=my_msg)
text_field.bind('<FocusIn>', on_entry_click)
text_field.bind("<Return>", send)
text_field.pack()
send_button = Button(root, text="Send", command=send)
send_button.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)

#Code for host ip and port (to be changed in the commercial version so no input is needed
HOST = input('Enter host: ')
PORT = input('Enter port: ')

if not PORT: #to be removed for non test version (no input needed for the final release)
    PORT = 33002
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT) #address defining

#Connection and thread handling

client_socket = socket.socket(AF_INET, SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
root.mainloop()
