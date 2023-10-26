import socket

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketTCP.bind(("127.0.0.1", 2023))

while(True):
    socketTCP.listen()
    print("Servidor TCP está esperando conexões!")

    socketCliente, endereco = socketTCP.accept()
    print(f"Endereço do cliente {endereco}")

    request = socketCliente.recv(1024).decode()

    print(request)
    response = 'HTTP/1.0 200 OK\n\n<h1>Hello World</h1>'

    socketCliente.sendall(response.encode())
    socketCliente.close()