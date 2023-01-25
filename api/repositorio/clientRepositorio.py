from models.Client import Client
class clientRepositorio:
    def listaClientes():
        clientes_objetos = Client.query.all()
        clientes_json = [cliente.to_json() for cliente in clientes_objetos]
        return clientes_json
