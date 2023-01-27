import configGeral
from repositorio.simulacaoRepositorio import simulacaoRepositorio
class simulacaoController:
    def listarSegmentos():
        try:
            return configGeral.jsonify({
                'status':'success',
                'data':[
                    {
                        'segment_code':3,
                        'tipo':'Carro ou Moto'
                    },
                    {
                        'segment_code':6,
                        'tipo':'Cirurgia Plástica ou Estética'
                    },
                    {
                        'segment_code':6,
                        'tipo':'Reforma'
                    },
                    {
                        'segment_code':6,
                        'tipo':'Viagem'
                    },
                    {
                        'segment_code':6,
                        'tipo':'Outros Serviços'
                    },
                ]
            })
        except Exception:
            return configGeral.jsonify({'status':'exception','data':Exception})

    def listarPlanos(idSegmento):
        try:
            return configGeral.jsonify({
                'status':'success',
                'data':simulacaoRepositorio.listarPlanosPorSegmento(idSegmento)
            })
        except Exception:
            return configGeral.jsonify({'status':'exception','data':Exception})  

    def listarParcelas(idSegmento, idPlano):
        try:
            return configGeral.jsonify({
                'status':'success',
                'data':simulacaoRepositorio.listarParcelaPorPlano(idSegmento, idPlano)
            })
        except Exception:
            return configGeral.jsonify({'status':'exception','data':Exception}) 
        
    def conferirEscolha(idParcela):
        try:
            return configGeral.jsonify({
                'status':'success',
                'data':simulacaoRepositorio.listarDadosParcelaEscolhida(idParcela)
            })
        except Exception:
            return configGeral.jsonify({'status':'exception','data':Exception}) 

    def listarEnderecos(cep):
        try:
            # if simulacaoRepositorio.listarEnderecos(cep)=='cep invalido':
            #     return configGeral.jsonify({'status':'invalido','data':'cep invalido'}) 
            return configGeral.jsonify({
                'status':'success',
                'data':simulacaoRepositorio.listarEnderecos(cep)
            })
        except Exception:
            return configGeral.jsonify({'status':'exception','data':Exception}) 

    def gravarCadastro():
        try:
            return configGeral.jsonify({
                'status':'success',
                'data':simulacaoRepositorio.gravarCadastro()
            })
        except Exception:
            return configGeral.jsonify({'status':'exception','data':Exception}) 