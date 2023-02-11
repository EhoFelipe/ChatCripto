# -*- coding: utf-8 -*-
import socket
import rsa

# Define o endereço IP e a porta do servidor
HOST = 'localhost'
PORTA = 50000

# Inicializa o socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta-se ao servidor
client.connect((HOST, PORTA))
data = client.recv(1024).decode().split(" ")
  print("Chave publica:  n= "+data[0]+" e= "+data[1])

# Envia mensagens ao servidor
while True:
    message = input("Digite a mensagem: ")
    msgcript = rsa.cipher(message,int(data[1]),int(data[0]))
    criptSTR = " ".join(msgcript)
    client.send(criptSTR.encode())
    client.sendall(str.encode(message))

socket.close()
