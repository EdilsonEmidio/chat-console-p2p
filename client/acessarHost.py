import socket
import json
import variaveis

def acessar(dados):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    server_address = (variaveis.host_endereco, variaveis.host_porta) #servidor que vai ser acessado
    sock.connect(server_address)
    sock.sendall(json.dumps(dados).encode("utf-8")) 
    data = sock.recv(2048).decode("utf-8")
    return data


