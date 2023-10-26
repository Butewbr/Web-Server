import socket # Importamos a biblioteca socket

if __name__ == "__main__": # Iniciamos o main
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Instanciamos a variável do Socket

    socketTCP.bind(("127.0.0.1", 2023)) # Conectamos o socket ao endereço e porta

    while(True): # Iniciamos o loop
        socketTCP.listen() # Ouvimos a porta
        print("Servidor TCP está esperando conexões!") # Printamos que o servidor está esperando conexções

        socketCliente, endereco = socketTCP.accept() # Aceitamos uma requisição
        print(f"Endereço do cliente {endereco}") # Printamos o endereço do cliente

        request = socketCliente.recv(1024).decode() # Recebemos a mensagem do cliente

        print(request) # Printamos a requisição
        response = 'HTTP/1.0 200 OK\n\n<h1>Hello World</h1>' # Geramos uma resposta

        socketCliente.sendall(response.encode()) # Enviamos a resposta ao client
        socketCliente.close() # Fechamos o socket do client