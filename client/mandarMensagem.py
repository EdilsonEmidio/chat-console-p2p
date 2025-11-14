import socket
import classes
import json

def pegarMensagem(tipo, lista_todos : list[classes.Usuario]):
    while True:
        print("/exit para sair")
        print("pode digitar sua mensagem:")
        mensagem = input()
        if mensagem == "/exit":
            break; 
        if tipo==0:
            mandarPublico(mensagem, lista_todos)

def mandarPublico(mensagem :str, lista_todos : list[classes.Usuario]):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    for usuario in lista_todos:
        data = {
			"tipo":"p",#p de publico
			"data":mensagem
		}
        sock.connect(("localhost", ("500",usuario.id))) 
        sock.sendall(json.dumps(data).encode("utf-8"))
