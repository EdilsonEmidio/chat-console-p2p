
class Usuario:
    
    def __init__(self, cliente, address, id, nome):
        self.cliente = cliente
        self.address = address
        self.id = id
        self.nome = nome
    
    
class ListaUsuarios:
    
    def __init__(self):
        self.lista_usuarios: list[Usuario] = []
        
    def getUsuarios(self, id):
        for usuario in self.lista_usuarios:
            if usuario.id == id:
                todos_sem_ele = self.lista_usuarios.remove(usuario)
                self.lista_usuarios.append(usuario)
                return todos_sem_ele
        return self.lista_usuarios
    
    def setUsuario(self, usuario: Usuario, id):
        if not self.usuarioExiste(id):
            self.lista_usuarios.append(usuario)
        else:
            print("ERRO, usuario ja existe!")
        
    def usuarioExiste(self, id):
        for usuario in self.lista_usuarios:
            if usuario.id == id:
                return True
        return False
    
class Grupo:
    def __init__(self, id, nome, membros: list[Usuario], adms: list = [Usuario]) -> None:
        self.id = id
        self.nome = nome
        self.membros = membros
        self.admins= []
        for adm in adms:
            self.admins.append(adm)
            
    def addAdmin(self, adm: Usuario):
        self.admins.append(adm)
    
    def removeAdmin(self, adm: Usuario):
        self.admins.remove(adm)
    
class ListaGrupos:
    
    def __init__(self, ) -> None:
        self.lista_grupos: list[Grupo] = []
    
    
    
        
    def removeAdmin(self, id_grupo, adm: Usuario):
        self.lista_grupos.__getitem__()