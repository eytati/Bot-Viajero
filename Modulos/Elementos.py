'''
class Usuario(object):
    def esta_authenticated(self):
        return True

    def esta_activa(self):
        return True

    def es_anonimo(self):
        return False

    def get_id(self):
        try:
            return str(self.id)
        except ArithmeticError:
            raise NotImplementedError('No id')

    def __eq__(self, otro):
        igual = self.__eq__(otro)
        if igual is NotImplemented:
            return NotImplemented
        return not igual

    def __ne__(self, other):
        igual = self.__eq__(other)
        if igual is NotImplemented:
            return NotImplemented
        return not igual
'''