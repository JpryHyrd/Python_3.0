import select
from threading import Thread, Lock
import time
from socket import socket, AF_INET, SOCK_STREAM

t = Thread(target="chat")
done = Lock()

def read():
    try:
        data = socket.recv(1024).decode("ascii")
        print(data)
    except:
        time.sleep(1)
        pass

def write():
    msg = input("Cooбщение: ")
    socket.send(msg.encode("ascii"))
    time.sleep(1)



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
if __name__ == "__main__":
    t.daemon = True
    t.start()












