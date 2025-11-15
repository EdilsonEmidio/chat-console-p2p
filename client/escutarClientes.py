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
        
        nome = procurarNome(lista_todos, address)
        id_mensagem = procurarId(lista_todos, nome)
        dados = classes.Mensagem(id_mensagem, nome, data)
        
        if data.tipo == "publico":
            mensagens_publicas.append(dados)
        elif data.tipo == "privado":
            pass
        elif data.tipo == "grupo":
            pass
        cliente.close
    
def procurarNome(lista_todos: list[classes.Usuario], address):
    for usuario in lista_todos:
        print(address)
        if usuario.address == address:
            return usuario.nome

def procurarId(lista_todos: list[classes.Usuario], nome):
    for usuario in lista_todos:
        
        if usuario.nome == nome:
            return usuario.id
    
