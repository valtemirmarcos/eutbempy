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

    def valorCarta(segmento):
        try:
            return configGeral.render_template("valor_carta.html",ssegmento=segmento) 
        except Exception: 
            return configGeral.render_template("error.html",erro="Falha ao carregar os site") 

    def valorParcela(segmento, carta):
        try:
            return configGeral.render_template("valor_parcela.html",ssegmento=segmento, scarta=carta) 
        except Exception: 
            return configGeral.render_template("error.html",erro="Falha ao carregar os site") 

    def conferir(idPlano):
        try:
            return configGeral.render_template("conferir.html",sidPlano=idPlano) 
        except Exception: 
            return configGeral.render_template("error.html",erro="Falha ao carregar os site") 

    def cadastro(idPlano):
        try:
            return configGeral.render_template("cadastro.html",sidPlano=idPlano) 
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