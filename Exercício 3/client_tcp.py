import socket # Importamos a biblioteca socket
from threading import Thread # Importamos Thread

def send_request(msgToSend): # Definimos uma função para envio de requisição
    print("NEW THREAD STARTED!") # Printamos que uma nova thread foi iniciada
    
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Instanciamos a variável do Socket

    socketTCP.connect(("127.0.0.1", 2023)) # Conectamos o socket ao endereço e porta

    socketTCP.sendall(str.encode(msgToSend)) # Enviamos a mensagem ao servidor

    msg = socketTCP.recv(1024) # Recebemos a resposta do servidor

    if not msg: # Verificamos se alguma mensagem foi retornada
        print("Server closed the connection.") # Se não houve resposta, printamos que o servidor foi desligado
        socketTCP.close() # Fechamos o socket
        return # Retornamos

    print(f"Received {msg!r}") # Se alguma resposta chegou, printamos no terminal
    
    socketTCP.close() # Fechamos o socket

if __name__ == "__main__": # Iniciamos o main
    n_of_requests = int(input("Digite a quantidade de requisições a serem feitas (entre 1 e 30): ")) # Pedimos um número de requisições a serem feitas ao servidor

    for i in range(n_of_requests): # Criamos um loop para pedir diferentes requisições 
        if i%2 == 0: # Caso o loop esteja em uma iteração par
            thread = Thread(target = send_request("GET /aaa HTTP/1.1")) # A requisição será feita para uma página não existente, retornando o 404.html
        elif i%3 == 0: # Caso o loop esteja em uma iteração múltipla de 3
            thread = Thread(target = send_request("GET /request HTTP/1.1")) # A requisição será feita para a página request
        else: # Para o resto
            thread = Thread(target = send_request("GET / HTTP/1.1")) # A requisição será feita para a página inicial
        
        thread.start() # A thread é iniciada