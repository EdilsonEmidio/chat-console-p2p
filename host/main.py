import socket
import usuarios
import json

def ligar():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(('192.168.3.2', 5050)) #aqui vai o ipv4 da maquina host na rede e sua porta
    
    server.listen(5)
    print("servidor aberto na porta 5050")
    
    todos_usuarios = usuarios.ListaUsuarios()
    id = 0
    
    while True:
        cliente, address = server.accept()
        data = cliente.recv(2048).decode("utf-8") #ele tem que passar o nome dele e o id
        data = json.loads(data)
        if data.id == -1:
            usuario_novo = usuarios.Usuario(cliente, address, id, data.nome)
            todos_usuarios.setUsuario(usuario_novo, id)
        
        id_usuario = id if data.id==-1 else data.id
        response = {
            "id": id_usuario, #id que o usuario vai receber, caso tente acessar de novo
            "data":todos_usuarios.getUsuarios(id_usuario)
        }
        id += 1
        cliente.send(json.dumps(response).encode("utf-8")) #manda o lista de todos os usuarios
        cliente.close
    
ligar()