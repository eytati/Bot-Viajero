#from passlib.apps import custom_app_context as pwd_context
from passlib.hash import sha256_crypt

class feature_password():

    def hash_password(self, password):
         return sha256_crypt.hash(password)

    def verify_password(self, password, password2):
        return sha256_crypt.verify(password, password2)

