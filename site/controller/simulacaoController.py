import configGeral
class simulacaoController:
    def index():
        try:
            return configGeral.render_template("index.html",nada='') 
        except Exception: 
            return configGeral.render_template("error.html",erro="Falha ao carregar os site") 

    def projeto():
        try:
            return configGeral.render_template("projeto.html",nada='') 
        except Exception: 
            return configGeral.render_template("error.html",erro="Falha ao carregar os site") 

    def valorCarta():
        try:
            return configGeral.render_template("valor_carta.html",nada='') 
        except Exception: 
            return configGeral.render_template("error.html",erro="Falha ao carregar os site") 

    def valorParcela():
        try:
            return configGeral.render_template("valor_parcela.html",nada='') 
        except Exception: 
            return configGeral.render_template("error.html",erro="Falha ao carregar os site") 

    def conferir():
        try:
            return configGeral.render_template("conferir.html",nada='') 
        except Exception: 
            return configGeral.render_template("error.html",erro="Falha ao carregar os site") 

    def cadastro():
        try:
            return configGeral.render_template("cadastro.html",nada='') 
        except Exception: 
            return configGeral.render_template("error.html",erro="Falha ao carregar os site") 

    def pagar():
        try:
            return configGeral.render_template("pagar.html",nada='') 
        except Exception: 
            return configGeral.render_template("error.html",erro="Falha ao carregar os site") 

    def finalizado():
        try:
            return configGeral.render_template("finalizado.html",nada='') 
        except Exception: 
            return configGeral.render_template("error.html",erro="Falha ao carregar os site") 