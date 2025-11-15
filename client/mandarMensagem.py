import socket
import classes
import json
import classes
import mostrarMensagens

def pegarMensagem(id, autor, tipo, lista_todos : list[classes.Usuario], id_privado=None):
    mensagens_enviadas : list[classes.Mensagem] = []
    while True:
        

        print("/exit para sair")
        print("pode digitar sua mensagem:")
        entrada = input()
        mensagem = classes.Mensagem(id, autor, entrada)
        if entrada == "/exit":
            break; 
        if tipo==0:
            mandarPublico(mensagem, lista_todos)
        elif tipo==1:
            #mandarGrupoPrivado
            pass
        elif tipo==2:
          mandarPrivado(mensagem,id_privado)  
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



def mandarPrivado(mensagem :classes.Mensagem, id_privado):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    data = {
			"tipo":"privado",
			"data":mensagem
		}
    sock.connect(("localhost", ("500",id_privado)))
    sock.sendall(json.dumps(data).encode("utf-8"))