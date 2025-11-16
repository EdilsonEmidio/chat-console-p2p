import json
import view
import acessarHost
import escutarClientes
import threading
import classes
import mandarMensagem
import mostrarMensagens

id = -1
nome = "edilson"
lista_todos: list[classes.Usuario] = []
online = False
address = None

parar = threading.Event()


mensagens_publicas: list[classes.Mensagem] = []
mensagens_privadas: list[classes.Mensagem]= []
mensagens_grupo: list[classes.Grupo] = []
grupos: list = []



while True:
    entrada = view.opcoes()
    if online:
        thread_secundaria = threading.Thread(
            target = escutarClientes.conectarP2P, 
            args=(parar, lista_todos, id, address , mensagens_publicas, mensagens_privadas, mensagens_grupo),
            name="thread-1"
        )
        thread_secundaria.start()
        
    if entrada == 2:#acessar o host e pegar quem tá online
        dados = {
            "nome":nome,
            "id":id
        } 
       
        data = json.loads(acessarHost.acessar(dados))
        lista_todos = data["data"]
        id = data["id"]
        address = data["address"][0]
        online = True
        
    elif entrada == 3:
        
        while True:
            entrada2 = view.opcoesCliente()
            if entrada2 == 2: #chat publico aqui
                mostrarMensagens.publico(mensagens_publicas)
                mensagens = mandarMensagem.pegarMensagem(id, nome, 0, lista_todos, mensagens_publicas)#0 é tipo publico
                mensagens_publicas.extend(mensagens)
                
            elif entrada2 == 3:
                while True:
                    entrada3 = view.opcoesGrupoPrivado()
                    if entrada3 == 2:
                        pass
                    elif entrada3 == 3:
                        pass
                    elif entrada3 == 4:
                        pass
                    elif entrada3 == 5:
                        break
                
            elif entrada2 == 4:
                while True:
                    entrada3 = view.opcoesConversaPrivada()
                    if entrada3 == 2:
                        if lista_todos != None:
                            view.mostrarPessoasOnline(lista_todos)
                        else:
                            print("não há outras pessoas online")
                    elif entrada3 == 3:
                        
                        print("digite o id de quem quer conversar:")
                        id_amigo = input()
                        mostrarMensagens.privado(mensagens_privadas, id_amigo, id)
                        mandarMensagem.pegarMensagem(id, nome, 2, lista_todos)
                    elif entrada3 == 4:
                        break
                    
            elif entrada2 == 5:
                break
        
    elif entrada == 4:
        break
parar.set()

def atualizar():
    pass

