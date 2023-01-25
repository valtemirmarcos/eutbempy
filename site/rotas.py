import configGeral
from controller.simulacaoController import simulacaoController

app = configGeral.app

@app.route('/')
def index():
    return simulacaoController.index() 
@app.route('/projeto')
def projeto():
    urlget = configGeral.request.path
    configGeral.session['navega'] = urlget
    if configGeral.session.get('navega')!=urlget:
        return configGeral.redirect('/')
    
    return simulacaoController.projeto() 
@app.route('/valorCarta')
def valorCarta():
    return simulacaoController.valorCarta() 
@app.route('/valorParcela')
def valorParcela():
    return simulacaoController.valorParcela() 
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
