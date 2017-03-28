
class base_de_datos:
    matriz = []
    instance = None
#-------------------------------------Inicio de constructor------------------------------------------------------------#
    def __init__(self):
        if not base_de_datos.instance:
            base_de_datos.instance = self
#----------------------------------------Fin de constructor-----------------------------------------------------------#


#------------------------------------Aumenta el tamaño de la memoria segun sea necesario-------------------------------#
    def aumentar_espacio_en_lista(self):

        if len(self.matriz) is 0:
            self.matriz.append([])
            self.matriz[0].append(None)
        else:
            largo_matriz = len(self.matriz)
            self.matriz.append([])
            for agregar_las_columnas in range(0, largo_matriz):
                self.matriz[len(self.matriz) - 1].append(None)

            for lineas in range(0, len(self.matriz)):
                for columnas in range(0, len(self.matriz[lineas])):
                    if columnas is len(self.matriz[lineas]) - 1:
                        self.matriz[lineas].append(None)
                        break

#------------------------------------Fin de aumentar el tamaño de la memoria-------------------------------------------#


#------------------------------Es el metodo para guardar los datos en la memoria---------------------------------------#

    def agregar_usuarios(self, persona):
        ingreso_en_matriz = False
        for lineas in range(0, len(self.matriz)):
            if ingreso_en_matriz:
                break

            for columna in range(len(self.matriz[lineas])):
                if self.matriz[lineas][columna] is None:
                    self.matriz[lineas][columna] = persona
                    ingreso_en_matriz = True
                    break
        if not ingreso_en_matriz:
            self.aumentar_espacio_en_lista()
            self.matriz[0][len(self.matriz) - 1] = persona

#------------------------------Fin del metodo para guardar los datos en la memoria-------------------------------------#


#------------------------------Inicio del metodo para borrar los datos en la memoria-----------------------------------#
    def borrar_usuarios(self, persona):
        desaprede = False
        for linea in range(0, len(self.matriz)):
            if desaprede is True:
                break
            for columna in range(0, len(self.matriz[linea])):
                if self.matriz[linea][columna] is not None:
                 if persona == self.matriz[linea][columna].get():
                    self.matriz[linea][columna] = None
                    desaprede = True
                    break
        return desaprede

    def verificar_usuario(self, usuario):
        existe = False
        respuesta= ''
        for linea in range(len(self.matriz)):
            if existe is True:
                break
            for columna in range(len(self.matriz[linea])):
                if not self.matriz[linea][columna] is None:
                    json_usuarios = self.matriz[linea][columna]
                    if usuario == json_usuarios['persona'].get('usuario'):
                        respuesta = True
                        print(respuesta)
                        existe = True
                        break
        return respuesta