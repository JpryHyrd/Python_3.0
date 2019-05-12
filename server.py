from socket import *
import time

s = socket(AF_INET, SOCK_STREAM) 
s.bind(('', 7777))               
s.listen(5)                       
                                                               
while True:
    client, addr = s.accept()
    data = client.recv(1000000)
    print('Сообщение: ', data.decode('utf-8'), ',\nОтправлено клиентом: ', addr)
    msg = 'Привет, клиент'
    client.send(msg.encode('utf-8'))
    client.close()

