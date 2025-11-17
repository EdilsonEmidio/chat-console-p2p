import classes


def publico(mensagens_publicas: list[classes.Mensagem]):
    for mensagem in mensagens_publicas:
        print("autor: ",mensagem.autor," - ",mensagem)
        print("")
        
def privado(mensagens_publicas: list[classes.Mensagem], id_amigo, id_seu):
    for mensagem in mensagens_publicas:
        if (mensagem.id == id_amigo or mensagem.id == id_seu):
            print("autor: ",mensagem.autor," - ",mensagem)
            print("")
            
def grupo(mensagens_grupo: list[classes.Grupo], id_amigo, id_seu):
    for mensagem in mensagens_grupo:
        if (mensagem.id == id_amigo or mensagem.id == id_seu):
            print("autor: ",mensagem.autor," - ",mensagem)
            print("")
            