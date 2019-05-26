import select
from socket import socket, AF_INET, SOCK_STREAM

def read():
    try:
        data = socket.recv(1024).decode("ascii")
        print(data)
    except:
        pass

def write():
    msg = input("Cooбщение: ")
    socket.send(msg.encode("ascii"))


s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", 8888))

name = input("Type your name: ")
while True:
    read()
    answer = input("1 - ввести сообщение; 2 - выход из чата, другое - обновить чат: ")
    if answer == "2":
        print("Жаль...")
        break
    elif answer == "1":
        write()
    else:
        continue













