from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from  Modulos import  Elementos2
import uuid

class usuario():
    db = Elementos2.base_de_datos()
    def agregar(self, usuario, password):
        id = uuid.uuid4()
        json_persona = {"persona": {"id": id,"usuario": usuario, "password": password}}
        self.db.agregar_usuarios(json_persona)
        print(json_persona)

    def verificar_usuario(self, usu):
        return self.db.verificar_usuario(usu)

    def generate_auth_token(self, usuario, expiration=700):
        serializacion = Serializer('Hola', expires_in=expiration)
        #Solicitar que retorne el usuario
        return serializacion.dumps({'id': self.db.verificar_usuario(usuario)})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer('Hola')
        try:
            data = s.loads(token)
        except SignatureExpired:
                return None  # valid token, but expired
        except BadSignature:
                return None  # invalid token
        #solicitar usuario
        db = Elementos2.base_de_datos()
        user = db.verificar_usuario(usuario)
        return user

