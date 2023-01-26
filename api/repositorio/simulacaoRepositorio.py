import configGeral
from models.InstallmentValue import InstallmentValue
import json
class simulacaoRepositorio:
    def listarPlanosPorSegmento(idSegmento):
        planos_objeto = InstallmentValue.query.filter(InstallmentValue.segment_code==idSegmento).filter(InstallmentValue.simulacao==1).order_by(InstallmentValue.credito_valor.asc()).distinct(InstallmentValue.credito_valor).group_by(InstallmentValue.credito_valor)
        lista = []
        for planos in planos_objeto:
            lista.append({
                'segment_code':planos.segment_code,
                'credito_valor':planos.credito_valor,
                'values_id':planos.values_id,
                'valor':configGeral.convertNumero(planos.credito_valor)
            })
        
        return lista
        
        # planos_json = [planos.to_json() for planos in planos_objeto]
        # return planos_json
    

    def listarParcelaPorPlano(idSegmento, idPlano):
        parcelas_objeto = InstallmentValue.query.filter(InstallmentValue.segment_code==idSegmento).filter(InstallmentValue.values_id==idPlano).filter(InstallmentValue.simulacao==1).order_by(InstallmentValue.credito_valor.asc()).distinct(InstallmentValue.credito_valor).group_by(InstallmentValue.parcelas_numero)
        lista = []
        for parcelas in parcelas_objeto:
            lista.append({
                'segment_code':parcelas.segment_code,
                'installment':parcelas.installment/100,
                'values_id':parcelas.values_id,
                'parcelas_numero':parcelas.parcelas_numero,
                'id':parcelas.id
            })
        
        return lista

    def listarDadosParcelaEscolhida(idParcela):
        parcelas_objeto = InstallmentValue.query.filter(InstallmentValue.id==idParcela).order_by(InstallmentValue.credito_valor.asc())

        lista = []
        for parcelas in parcelas_objeto:
            taxa = (parcelas.effective_tax/100)/parcelas.parcelas_numero
            lista.append({
                'segment_code':parcelas.segment_code,
                'installment':parcelas.installment/100,
                'values_id':parcelas.values_id,
                'parcelas_numero':parcelas.parcelas_numero,
                'id':parcelas.id,
                'credito_valor':parcelas.credito_valor,
                'total':parcelas.total,
                'total_pos_contemplacao':parcelas.total_pos_contemplacao,
                'effective_tax':parcelas.effective_tax,
                'taxa_mensal':float('{:.2f}'.format(taxa))
            })
        
        return lista