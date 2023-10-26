import socket

socketTCP = socket. socket(socket.AF_INET, socket.SOCK_STREAM)

socketTCP.bind(("127.0.0.1", 2023))

while(True):
    socketTCP.listen()
    print("Servidor TCP está esperando conexões!")

    socketCliente, endereco = socketTCP.accept()
    print(f"Endereço do cliente {endereco}")

    msg = socketCliente.recv(1024)

    print(msg)

    socketCliente.sendall(str.encode("Mensagem Recebida!"))

    if(msg.lower() == b"stop"):
        socketCliente.sendall(str.encode("\nShutting down server..."))  
        print("Shutting down server...")
        socketCliente.close()
        break