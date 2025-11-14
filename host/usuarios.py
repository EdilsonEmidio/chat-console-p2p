
class Usuario:
    
    def __init__(self, cliente, address, id, nome):
        self.cliente = cliente
        self.address = address
        self.id = id
        self.nome = nome
    
    
class ListaUsuarios:
    
    def __init__(self):
        self.lista_usuarios: list[Usuario] = []
        
    def getUsuarios(self):
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
    