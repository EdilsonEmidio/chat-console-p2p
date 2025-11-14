



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
        print("2 - grupo publico")
        print("3 - grupo privado")
        print("4 - conversa privada")
        print("5 - voltar")
        entrada = int(input())
    return entrada
