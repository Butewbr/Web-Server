import socket # Importamos a biblioteca socket

if __name__ == "__main__": # Iniciamos o main
    while(True): # Iniciamos o loop
        socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Instanciamos a variável do Socket

        socketTCP.connect(("127.0.0.1", 2023)) # Conectamos o socket ao endereço e porta

        msgToSend = input("Envie uma mensagem ao servidor (digite stop para fechar o servidor): ") # Pedimos ao usuário uma mensagem a ser enviada ao servidor

        socketTCP.sendall(str.encode(msgToSend)) # Enviamos a mensagem ao servidor

        msg = socketTCP.recv(1024) # Capturamos a mensagem de resposta do servidor

        print(f"Received {msg!r}") # Printamos ao usuário a resposta do servidor
        
        if not msg or msg == b"Shutting down server...": # Verificamos se nenhuma mensagem retornou ou se retornou um aviso de servidor sendo fechado
            print("Server closed the connection.") # Printamos ao usuário que o servidor fechou
            
            socketTCP.close() # Fechamos o socket
            break # Quebramos o loop