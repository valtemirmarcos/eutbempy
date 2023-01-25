from models.User import Users
class userRepositorio:
    def listaUsuarios():
        usuarios_objetos = Users.query.all()
        usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
        return usuarios_json
