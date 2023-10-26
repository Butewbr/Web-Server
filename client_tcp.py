import socket

socketTCP= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketTCP.connect( ("127.0.0.1", 2023))

msgToSend = input("Envie uma mensagem ao servidor: ")

socketTCP.sendall(bytes(msgToSend, 'utf-8'))

msg = socketTCP.recv(1024)
print (f"Received {msg!r}")

socketTCP.close()