import socket
import json

def acessar(dados):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    server_address = ("192.168.3.2", 5050) 
    sock.connect(server_address) 
    sock.sendall(json.dumps(dados).encode("utf-8")) 
    data = sock.recv(2048).decode("utf-8")
    return data


