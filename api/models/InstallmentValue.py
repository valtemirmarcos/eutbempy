import configGeral
from datetime import datetime
db = configGeral.dbConfig
class InstallmentValue(db.Model):
    __tablename__ = 'installments_values'

    id = db.Column(db.Integer, primary_key=True)
    values_id = db.Column(db.BigInteger)
    installments_id = db.Column(db.BigInteger)
    installment = db.Column(db.Integer)
    effective_tax = db.Column(db.Integer)
    administration_tax = db.Column(db.Integer)
    reserve_fund = db.Column(db.Integer)
    insurance_1 = db.Column(db.Integer)
    insurance_2 = db.Column(db.Integer)
    total = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime, default=datetime.now())
    plan_total = db.Column(db.Integer)
    ativo  = db.Column(db.String(1))
    segment_code = db.Column(db.String(191))
    credito_valor = db.Column(db.Integer)
    parcelas_numero = db.Column(db.Integer)
    effective_tax_pos_contemplacao = db.Column(db.Integer)
    administration_tax_pos_contemplacao = db.Column(db.Integer)
    total_pos_contemplacao = db.Column(db.Integer)
    tipo = db.Column(db.String(191))
    promocao_tipo_id = db.Column(db.Integer)
    deleted_at = db.Column(db.DateTime)
    simulacao  = db.Column(db.String(1))

    # def to_json(self):
    #     return {
    #         "id":self.id, 
    #         "values_id":self.values_id, 
    #         "installments_id":self.installments_id,
    #         "installment":self.installment,
    #         "effective_tax":self.effective_tax,
    #         "administration_tax":self.administration_tax,
    #         "reserve_fund":self.reserve_fund,
    #         "insurance_1":self.insurance_1,
    #         "insurance_2":self.insurance_2,
    #         "total":self.total,
    #         "created_at":str(self.created_at),
    #         "updated_at":str(self.updated_at),
    #         "deleted_at":str(self.deleted_at),
    #         "plan_total":self.plan_total,
    #         "ativo":self.ativo, 
    #         "segment_code":self.segment_code, 
    #         "credito_valor":self.credito_valor,
    #         "parcelas_numero":self.parcelas_numero,
    #         "effective_tax_pos_contemplacao":self.effective_tax_pos_contemplacao,
    #         "administration_tax_pos_contemplacao":self.administration_tax_pos_contemplacao,
    #         "total_pos_contemplacao":self.total_pos_contemplacao,
    #         "tipo":self.tipo,
    #         "promocao_tipo_id":self.promocao_tipo_id,
    #         "simulacao":self.simulacao
    #     }