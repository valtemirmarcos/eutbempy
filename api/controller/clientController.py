
import configGeral
from repositorio.clientRepositorio import clientRepositorio

class clientController:
    def listaClientes():
        # print(usuarios_objetos)
        return configGeral.jsonify({'mensagem':clientRepositorio.listaClientes()})
        # return Response(json.dumps(usuarios_json))