import socket

while(True):
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socketTCP.connect(("127.0.0.1", 2023))

    msgToSend = input("Envie uma mensagem ao servidor: ")

    socketTCP.sendall(str.encode(msgToSend))

    msg = socketTCP.recv(1024)

    print(f"Received {msg!r}")
    
    socketTCP.close()
    
    if not msg:
        print("Server closed the connection.")
        break

    if(msg == b"Shutting down server..."):
        print("Server closed the connection.")
        break