import socket
import asyncio
import threading
import classes
import main

def conectarP2P(parar: threading.Event, lista_todos: list[classes.Usuario], id):
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost', int('500',id)))

    server.listen(len(lista_todos))
    
    mensagens_publicas: list[classes.Mensagem] = []
    mensagens_privadas: list[classes.Mensagem]= []
    mensagens_grupo: list[classes.Grupo] = []

    
    while parar:
        cliente, address = server.accept()
        data = cliente.recv(2048).decode("utf-8")
        nome = procurarNome(lista_todos, address)
        id_mensagem = procurarId(lista_todos, nome)
        dados = classes.Mensagem(id_mensagem, nome, data)
            
        mensagens_publicas.append(dados)
        cliente.close
        
        main.atualizar()
    
def procurarNome(lista_todos: list[classes.Usuario], address):
    for usuario in lista_todos:
        print(address)
        if usuario.address == address:
            return usuario.nome

def procurarId(lista_todos: list[classes.Usuario], nome):
    for usuario in lista_todos:
        
        if usuario.nome == nome:
            return usuario.id
    
