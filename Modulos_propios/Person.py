
from passlib.hash import sha256_crypt
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature)

class User():

    def new_user(self, string_connection, user, password):
        collection_users= string_connection.db.Usuarios
        json_person = {"user": user, "password": password, "token": ""}
        collection_users.insert(json_person)
        print(json_person)

    def verify_user(self, string_connection, user):
        collection_users = string_connection.db.Usuarios
        user_db = collection_users.find_one({"user": user})
        if user_db is None:
            return True
        return False

    def verify_user_password(self):
        print("")


class Password():

    def hash_password(self, password):
        return sha256_crypt.hash(password)

    def verify_password(self, password, password2):
        return sha256_crypt.verify(password2, password)



class Token():

    def generate_auth_token(self, user, expiration=700):
        serializacion = Serializer(user, expires_in=expiration)
        return serializacion.dumps({'Usuario': user})

    def get_information(self, string_connection, user):
       collection_users = string_connection.db.Usuarios
       data =  collection_users.find_one({"user": user})
       return data

    @staticmethod
    def verify_auth_token(user, token):
        serialization = Serializer(user)
        try:
            data = serialization.loads(token)
        except SignatureExpired:
            return  'Expiro Token' # valid token, but expired
        except BadSignature:
            return 'Token erroneo'  # invalid token
        return True
