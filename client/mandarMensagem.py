import socket
import classes
import json
import classes

def pegarMensagem(id, nome, tipo, lista_todos : list[classes.Usuario]):
    mensagens_enviadas : list[classes.Mensagem] = []
    while True:
        print("/exit para sair")
        print("pode digitar sua mensagem:")
        entrada = input()
        mensagem = classes.Mensagem(id, nome, entrada)
        if entrada == "/exit":
            break; 
        if tipo==0:
            mandarPublico(mensagem, lista_todos)
        
        mensagens_enviadas.append(mensagem)
    return mensagens_enviadas

def mandarPublico(mensagem :classes.Mensagem, lista_todos : list[classes.Usuario]):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    for usuario in lista_todos:
        data = {
			"tipo":"publico",
			"data":mensagem
		}
        sock.connect(("localhost", ("500",usuario.id))) 
        sock.sendall(json.dumps(data).encode("utf-8"))
