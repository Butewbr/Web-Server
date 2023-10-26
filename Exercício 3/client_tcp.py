import socket
from threading import Thread

def send_request(msgToSend):
    print("NEW THREAD STARTED!")
    
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socketTCP.connect(("127.0.0.1", 2023))

    socketTCP.sendall(str.encode(msgToSend))

    msg = socketTCP.recv(1024)

    if not msg:
        print("Server closed the connection.")
        socketTCP.close()
        return

    print(f"Received {msg!r}")
    
    socketTCP.close()

n_of_requests = int(input("Digite a quantidade de requisições a serem feitas (entre 1 e 30): "))

for i in range(n_of_requests):
    if i%2 == 0:
        thread = Thread(target = send_request("GET /aaa HTTP/1.1"))    
    elif i%5 == 0:
        thread = Thread(target = send_request("GET /request HTTP/1.1"))    
    else:
        thread = Thread(target = send_request("GET / HTTP/1.1"))
    
    thread.start()
        