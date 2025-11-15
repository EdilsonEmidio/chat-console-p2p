import socket
import asyncio
import threading
import classes
import json

def conectarP2P(parar: threading.Event, lista_todos: list[classes.Usuario], id, mensagens_publicas: list[classes.Mensagem],
                mensagens_privadas: list[classes.Mensagem], mensagens_grupo: list[classes.Grupo]):
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost', int('500',id)))

    server.listen(len(lista_todos))    
    
    
    while parar:
        cliente, address = server.accept()
        data = json.loads(cliente.recv(2048).decode("utf-8"))

        mensagem = data.data
        
        if data.tipo == "publico":
            mensagens_publicas.append(mensagem)
        elif data.tipo == "privado":
            mensagens_privadas.append(mensagem)
        elif data.tipo == "grupo":
            mensagens_grupo
        cliente.close
    
