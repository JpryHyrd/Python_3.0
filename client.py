from socket import *

s = socket(AF_INET, SOCK_STREAM)  
s.connect(('localhost', 7777))  
msg = input("Введите сообщение серверу: ")
s.send(msg.encode('utf-8'))
data = s.recv(1000000)
print('Сообщение от сервера: ', data.decode('utf-8'))
s.close()


