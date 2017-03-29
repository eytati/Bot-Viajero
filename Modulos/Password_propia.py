from passlib.apps import custom_app_context as pwd_context

class feature_password():

    def hash_password(self, password):
         pas =self.password_hash = pwd_context.encrypt(password)
         return pas

    def verify_password(self, password, password2):
        return pwd_context.verify(password, password2)
