
class Mensagem:
    def __init__(self, id, autor, mensagem) -> None:
        self.id = id
        self.autor = autor
        self.mensagem = mensagem
     
class Usuario:
    
    def __init__(self, cliente, address, id, nome):
        self.cliente = cliente
        self.address = address
        self.id = id
        self.nome = nome
       
class Grupo:
    def __init__(self, id_grupo, nome_grupo, membros: list[Usuario], lista_mensagens: list[Mensagem] = []) -> None:
        self.id_grupo = id_grupo
        self.nome_grupo = nome_grupo
        self.membros = membros
        self.lista_mensagens = lista_mensagens

