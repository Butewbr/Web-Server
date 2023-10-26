import socket # Importamos a biblioteca socket
from threading import Thread # Importamos Thread

def index(): # Definimos uma função para a rota Index
    HTMLFile = open("index.html", "r") # Abrimos o arquivo HTML
  
    index = HTMLFile.read() # Lemos o arquivo HTML
    
    return "HTTP/1.0 200 OK\n\n" + index # Retornamos a resposta como OK mais a página index.html

def seeRequest(request): # Definimos uma função para a rota seeRequest
    return f"HTTP/1.0 200 OK\n\n<h1>This is your request:</h1>\n<pre>${request}<pre>" # Retornamos a resposta como OK mais a requisição do usuário

def notFound(): # Definimos uma função para rotas não encontrada
    HTMLFile = open("404.html", "r") # Abrimos o arquivo HTML
  
    file = HTMLFile.read() # Lemos o arquivo HTML

    return "HTTP/1.0 404 NOT FOUND\n\n" + file # Retornamos a resposta como erro 404 mais a página de erro 404 

def handle_request(socketClient, endereco): # Criamos uam função para receber requisições
    print("NEW THREAD STARTED!") # Printamos que uma nova thread foi iniciada
    
    request = socketCliente.recv(1024).decode() # Recebemos a requisição

    print(request) # Printamos a requisição
    
    request_words = request.split() # Dividimos a requisição em uma lista de palavras
    
    try: # Fazemos uma busca na lista de palavras
        requested_page = request_words[request_words.index("GET") + 1] # Buscamos a rota pedida na requisição
        
        print("The page requested was: " + requested_page) # Printamos a página requisitada
        
        if requested_page == "/" or requested_page == "/index.html": # Se for a home
            response = index() # Enviamos como resposta a página index.html
        elif requested_page == "/request": # Se for a rota /request
            response = seeRequest(request) # Enviamos como resposta a página de visualização da requisição
        else: # Senão
            response = notFound() # Enviamos página de erro 404 - NOT FOUND
    except: # Caso a busca não seja bem sucedida, significa que não existe GET na requisição
        response = notFound() # Então retornamos página de erro 404 - NOT FOUND
        
    print("Response sent:\n" + response) # Ao fim printamos a resposta enviada

    socketCliente.sendall(response.encode()) # E enviamos a resposta ao client
    socketCliente.close() # Fechamos o socket

if __name__ == "__main__": # Iniciamos o main
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Instanciamos a variável do Socket

    socketTCP.bind(("127.0.0.1", 2023)) # Conectamos o socket ao endereço e porta

    while(True): # Iniciamos o loop
        socketTCP.listen() # Ouvimos a porta
        print("TCP server waiting...") # Printamos que o servidor está esperando conexções

        socketCliente, endereco = socketTCP.accept() # Aceitamos uma requisição
        print(f"User's address: {endereco}") # Printamos o endereço do cliente

        thread = Thread(target = handle_request(socketCliente, endereco)) # Criamos uma thread com as informações do client
        thread.start() # Iniciamos a thread