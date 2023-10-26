import socket # Importamos a biblioteca socket

if __name__ == "__main__": # Iniciamos o main
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Instanciamos a variável do Socket

    socketTCP.bind(("127.0.0.1", 2023)) # Ligamos o socket ao endereço e porta

    while(True): # Iniciamos o loop
        socketTCP.listen() # Ouvimos a porta
        print("Servidor TCP está esperando conexões!") # Printamos que o servidor está esperando conexções

        socketCliente, endereco = socketTCP.accept() # Aceitamos uma requisição
        print(f"Endereço do cliente {endereco}") # Printamos o endereço do cliente
        
        msg = socketCliente.recv(1024) # Recebemos a mensagem do cliente

        print(msg) # Printamos a mensagem

        if(msg.lower() == b"stop"): # Verificamos se é um pedido para fechar o servidor
            socketCliente.sendall(str.encode("Shutting down server...")) # Se sim, enviamos uma resposta de que o servidor está sendo desligado
            print("Shutting down server...") # Printamos que o servidor está sendo desligado

            socketCliente.close() # Fechamos o socket do client
            break # Quebramos o loop

        socketCliente.sendall(str.encode("Mensagem Recebida!")) # Enviamos uma resposta à mensagem do cliente