import select
from socket import socket, AF_INET, SOCK_STREAM

def read_requests(r_clients, all_clients):
    response = {}
    for sock in r_clients:
        try:
            data = socket.recv(1024).decode("ascii")
            response[sock] = data
        except:
            print("Клиент {} {} отключился".format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    return response

def write_response(requests, w_clients, all_clients):
    for sock in w_clients:
        if sock in requests:
            try:
                """resp = requests[sock].encode("ascii")
                test_len = sock.send(resp.upper())"""
                for sk in requests:
                    ln = requests[sk]
                    socket.send(ln.encode("ascii"))
            except:
                print("Клиент {} {} отключился".format(socket.fileno(), socket.getpeername()))
                sock.close()
                all_clients.remove(sock)
def mainloop():
    address = ("", 8888)
    clients = []
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(0.2)
    while True:
        try:
            conn, addr = s.accept()
        except OSError as e:
            pass
        else:
            print("Получен запрос на соединение от {}".format(str(addr)))
            clients.append(conn)
        finally:
            wait = 0
            r = []
            w = []
            try: 
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass
            requests = read_requests(r, clients)
            write_response(requests, w, clients)

print("Сервер запущен")
mainloop()

 





