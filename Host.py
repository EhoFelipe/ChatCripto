# -*- coding: utf-8 -*-
import socket
import rsa



HOST = 'localhost'
PORTA = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORTA))
server.listen()

connection = server.accept()

print(f"Aguardando conexao com Client")


client_socket, client_address = server.accept()
print(f"Conexao estabelecida com {client_address[0]}:{client_address[1]}")

p = int(input('Valor de p:'))
q = int(input('Valor de q:'))
n = p*q
a = rsa.totient(p)
b = rsa.totient(q)
n_totient = a*b
e = rsa.generate_E(n_totient)
connection.send((str(n)+" "+str(e)).encode())

chave_publica = (n, e)
print("Chave pubica:",chave_publica)
chave_privada =  rsa.calculate_private_key(n_totient,e)
print('Chave privada:', chave_privada)


while True:
    message = client_socket.recv(1024)
    message = rsa.descifra(message.split(" "), n, chave_privada)
    if not message:
        print('Terminando conexao')
        client_socket.close()
        break
    print(f"Mensagem recebida: {message}")
