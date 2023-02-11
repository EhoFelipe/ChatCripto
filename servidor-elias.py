import socket
import rsa 


def criandoCliente():

  HOST = socket.gethostname()     # Endereco IP do Servidor '127.0.0.1'
  PORT = 5000            # Porta que o Servidor esta
  cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  dest = (HOST, PORT)
  cliente.connect(dest)
  data = cliente.recv(1024).decode().split(" ")
  print("voce recebeu a chave publica do servidor:  n= "+data[0]+" e= "+data[1])
  print('Para sair use 0 para sair \n') 
  msg = ''
  while msg != '0':
      msg = input("digite uma nova menssagem:")
      cript = rsa.cipher(msg,int(data[1]),int(data[0]))
      criptSTR = " ".join(cript)
      cliente.send(criptSTR.encode())
      print("seu texto criptgrafado e:",cript)
  cliente.close()

criandoCliente()