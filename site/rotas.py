import configGeral
from controller.simulacaoController import simulacaoController
import json

app = configGeral.app
@app.route('/')
def index():
    configGeral.session['urlapi'] = configGeral.PATH_API
    return simulacaoController.index() 
@app.route('/projeto')
def projeto():

    # urlget = configGeral.request.url
    # teste2 = configGeral.request.args
    # print("urlget")
    # print(urlget)
    # print(teste2)
    # configGeral.session['navega'] = urlget
    # if configGeral.session.get('navega')!=urlget:
    #     return configGeral.redirect('/')
    
    return simulacaoController.projeto() 
@app.route('/valorCarta')
def valorCarta():
    parametros = configGeral.request.args
    if not parametros.get("segmento"):
        return configGeral.redirect('/projeto')
    return simulacaoController.valorCarta(parametros.get("segmento")) 
@app.route('/valorParcela')
def valorParcela():
    parametros = configGeral.request.args
    if not parametros.get("segmento") or not parametros.get("carta"):
        return configGeral.redirect('/projeto')
    return simulacaoController.valorParcela(parametros.get("segmento"), parametros.get("carta"))  
@app.route('/conferir')
def conferir():
    return simulacaoController.conferir() 
@app.route('/cadastro')
def cadastro():
    return simulacaoController.cadastro() 
@app.route('/pagar')
def pagar():
    return simulacaoController.pagar() 
@app.route('/finalizado')
def finalizado():
    return simulacaoController.finalizado() 
