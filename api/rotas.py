
import configGeral
from controller.userController import userController
from controller.clientController import clientController
from controller.simulacaoController import simulacaoController

app = configGeral.app

@app.route('/listaUsuarios', methods=["GET"])
def listaUsuarios():
    return userController.listaUsuarios()

@app.route('/listaClientes', methods=["GET"])
def listaClientes():
    return clientController.listaClientes()
@app.route('/listarSegmentos', methods=["GET"])
def listarSegmentos():
    return simulacaoController.listarSegmentos()
@app.route('/listarPlanos/<idSegmento>', methods=["GET"])
def listarPlanos(idSegmento):
    return simulacaoController.listarPlanos(idSegmento)
@app.route('/listarParcelas/<idSegmento>/<idPlano>', methods=["GET"])
def listarParcelas(idSegmento, idPlano):
    return simulacaoController.listarParcelas(idSegmento, idPlano)