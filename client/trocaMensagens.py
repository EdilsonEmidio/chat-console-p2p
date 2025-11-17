import classes

mensagens_publicas: list[classes.Mensagem] = []



def grupoPublico(lista_todos, id):
    pass

def mostrarChat(mensagens: list[classes.Mensagem]):
    for mensagem in mensagens:
        print(mensagem.autor, ": ", mensagem.mensagem)
        

