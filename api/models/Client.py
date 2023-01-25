import configGeral
from datetime import datetime
from models.User import Users
db = configGeral.dbConfig
class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'))
    first_name = db.Column(db.String(191))
    last_name = db.Column(db.String(191))
    phone = db.Column(db.String(191))
    usuarios = db.relationship('Users', backref='users', lazy=False)

    def to_json(self):
        return {
            "id":self.id, 
            "user_id":self.user_id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "phone":self.phone,
            "email":self.usuarios.email
        }