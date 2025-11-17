import socket
import usuarios
import json
import variaveis


def ligar():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((variaveis.host_endereco, variaveis.host_porta))
    
    server.listen(5)
    print("servidor aberto na porta ",variaveis.host_porta)
    
    todos_usuarios = usuarios.ListaUsuarios()
    todos_grupos = 
    id = 0
    
    while True:
        cliente, address = server.accept()
        data = cliente.recv(2048).decode("utf-8") #ele tem que passar o nome dele e o id
        data = json.loads(data)

        if data["id"] == -1:
            usuario_novo = usuarios.Usuario(cliente, address, id, data["nome"])
            todos_usuarios.setUsuario(usuario_novo, id)
        
        id_usuario = id if data["id"] ==-1 else data["id"]
        response = {
            "id": id_usuario, #id que o usuario vai receber, caso tente acessar de novo
            "data":todos_usuarios.getUsuarios(id_usuario),
            "address":address
        }
        id += 1
        cliente.send(json.dumps(response).encode("utf-8")) #manda o lista de todos os usuarios
        cliente.close
        print("conversou com alguem")
    
ligar()