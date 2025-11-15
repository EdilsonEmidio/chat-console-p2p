import classes


def opcoes() -> int:
    entrada = 0
    while entrada< 1 or entrada>4:
        print("1 - help")
        print("2 - acessar host")
        print("3 - acessar clientes")
        print("4 - sair")
        entrada = int(input())
    return entrada

def opcoesCliente() -> int:
    entrada = 0
    while entrada< 1 or entrada>5:
        print("1 - help")
        print("2 - chat publico")
        print("3 - grupo privado")
        print("4 - chat privado")
        print("5 - voltar")
        entrada = int(input())
    return entrada

def opcoesGrupoPrivado() -> int:
    entrada = 0
    while entrada< 1 or entrada>5:
        print("1 - help")
        print("2 - ver grupos")
        print("3 - criar grupo")
        print("4 - entrar em grupo")
        print("5 - voltar")
        entrada = int(input())
    return entrada


def opcoesConversaPrivada() -> int:
    entrada = 0
    while entrada< 1 or entrada>4:
        print("1 - help")
        print("2 - pessoas online")
        print("3 - mandar mensagem")
        print("4 - voltar")
        entrada = int(input())
    return entrada

def mostrarPessoasOnline(lista_pessoas : list[classes.Usuario]):
    print("usuarios online:")
    for usuario in lista_pessoas:
        print("usuario: ",usuario.nome, " - id:", usuario.id)
    
    