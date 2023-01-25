
import configGeral
from repositorio.userRepositorio import userRepositorio

class userController:
    def listaUsuarios():
        # print(usuarios_objetos)
        return configGeral.jsonify({'mensagem':userRepositorio.listaUsuarios()})
        # return Response(json.dumps(usuarios_json))