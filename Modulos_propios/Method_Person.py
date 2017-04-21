from Modulos_propios import   Person
from flask import request, jsonify

class Conexion_con_datos():
 #------------------------------Metodo de crear usuarios---------------------------------------------------------------#
    def create_user(self, string_connection):

        Users = Person.User()
        Passwords= Person.Password()
        print(request.json)

        username = request.json.get('username')
        password = request.json.get('password')
        repassword = request.json.get('repassword')

        if username is None or password is None:  #
            return jsonify({"Error": "Faltan datos"})

        allow_user = Users.verify_user(string_connection, username)
        if not allow_user is True:
            return jsonify({"Error": "Usuario ya existe"})

        if not password == repassword:
           return jsonify({"Error": "'Las contraseñas no coinciden'"})

        password_hash = Passwords.hash_password(password)

        Users.new_user(string_connection, username, password_hash)

        return jsonify({'username': username})

#------------------------------Metodo de autenticar--------------------------------------------------------------------#
    def authentication(self, string_connection, username, password):

        Users = Person.User()
        Passwords = Person.Password()
        Tokens = Person.Token()

        if username is None or password is None:  #
            return jsonify({"Error": "Faltan datos"})

        allow_user = Users.verify_user(string_connection, username)
        if  allow_user is True:
            return jsonify({"Error": "Usuario no existe"})

        data_db =  Tokens.get_information(string_connection, username)

        password_db=  data_db['password']
        allow_password = Passwords.verify_password(password_db, password)

        if allow_password is True:
            return True
        return  jsonify({"Error": "Contraseña incorrecta"})

#-------------------------------------------Generar token------------------------------------------------------------#
    def generate_token(self, string_connection, user, expiration):

        Tokens = Person.Token()
        token = Tokens.generate_auth_token(user, expiration)
        token = token.decode('ascii')

        collection_users = string_connection.db.Usuarios
        data_db = Tokens.get_information(string_connection, user)

        username_db = data_db["user"]
        collection_users.update_one({"user": username_db},  {'$set': {'token': str(token) }},upsert=False)

        return token

#-------------------------------------------Verificar token------------------------------------------------------------#
    def verify_token(self, string_connection, token):
        collection_users = string_connection.db.Usuarios
        data_user = collection_users.find_one({"token": token})
        if not data_user is None:
            user = data_user["user"]
            Tokens = Person.Token()
            return Tokens.verify_auth_token(user, token)

        return jsonify({"Error": "Token expirado"})