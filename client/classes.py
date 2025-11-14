
class Mensagem:
    def __init__(self, id, autor, mensagem) -> None:
        self.id = id
        self.autor = autor
        self.mensagem = mensagem
        
class Grupo:
    def __init__(self, nome_grupo, lista_mensagens: list[Mensagem]) -> None:
        self.nome_grupo = nome_grupo
        self.lista_mensagens = lista_mensagens

class Usuario:
    
    def __init__(self, cliente, address, id, nome):
        self.cliente = cliente
        self.address = address
        self.id = id
        self.nome = nome
    