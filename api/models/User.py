import configGeral
from datetime import datetime
db = configGeral.dbConfig
class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(191))
    email = db.Column(db.String(191))
    role_id = db.Column(db.BigInteger)
    avatar = db.Column(db.String(191))
    email_verified_at = db.Column(db.DateTime)
    password = db.Column(db.String(191))
    remember_token = db.Column(db.String(100))
    settings = db.Column(db.Text)
    api_token = db.Column(db.String(191))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime, default=datetime.now())
    deleted_at = db.Column(db.DateTime)
    partner_id = db.Column(db.BigInteger)

    def to_json(self):
        return {
            "id":self.id, 
            "name":self.name, 
            "email":self.email,
            "role_id":self.role_id,
            "avatar":self.avatar,
            "email_verified_at":str(self.email_verified_at),
            "password":self.password,
            "remember_token":self.remember_token,
            "settings":self.settings,
            "api_token":self.api_token,
            "created_at":str(self.created_at),
            "updated_at":str(self.updated_at),
            "deleted_at":str(self.deleted_at),
            "partner_id":self.partner_id,
        }