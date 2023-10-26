import socket
from threading import Thread

def index():
    HTMLFile = open("index.html", "r") 
  
    # Reading the file 
    index = HTMLFile.read()
    
    return "HTTP/1.0 200 OK\n\n" + index

def seeRequest(request):
    return f"HTTP/1.0 200 OK\n\n<h1>This is your request:</h1>\n<pre>${request}<pre>"

def notFound():
    HTMLFile = open("404.html", "r") 
  
    # Reading the file 
    file = HTMLFile.read()
    
    return "HTTP/1.0 404 OK\n\n" + file

def handle_request(socketClient, endereco): 
    print("NEW THREAD STARTED!")
    
    request = socketCliente.recv(1024).decode()

    print(type(request))

    print(request)
    
    request_words = request.split()
    
    try:
        requested_page = request_words[request_words.index("GET") + 1]
        
        print("The page requested was: " + requested_page)
        
        if requested_page == "/" or requested_page == "/index.html":
            response = index()
        elif requested_page == "/request":
            response = seeRequest(request)
        else:
            response = notFound()
    except:
        response = notFound()
        
    print("Response sent:\n" + response)

    socketCliente.sendall(response.encode())
    socketCliente.close()

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketTCP.bind(("127.0.0.1", 2023))

while(True):
    socketTCP.listen()
    print("TCP server waiting...")

    socketCliente, endereco = socketTCP.accept()
    print(f"User's address: {endereco}")

    thread = Thread(target = handle_request(socketCliente, endereco))
    thread.start()