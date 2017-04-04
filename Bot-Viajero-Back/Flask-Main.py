from flask import Flask
from flask_httpauth import  HTTPBasicAuth
from flask.ext.pymongo import  PyMongo
from Modulos import Metodos_de_flask
from  Modulos import Usuario
from  Modulos import Password_propia


#--------------------------------------------Inicio del codigo---------------------------------------------------------#

app = Flask(__name__)

#--------------------------------------------Para utilizar la autenticacion--------------------------------------------#
registro_auth = HTTPBasicAuth()

#------------------------------------------Conexion con la base de datos-----------------------------------------------#
app.config['Direccion_BD'] = 'mongodb://<BotViajero>:<bot5917>@ds135800.mlab.com:35800/botviajero'
db = PyMongo(app)

#----------------------------------Instancia de la clase de los metodos de flask---------------------------------------#
metodos = Metodos_de_flask.Metodos_requeridos()

#---------------------------------------------Registro en la base de datos---------------------------------------------#
@app.route('/api/registrar/persona', methods = ['POST'])
def nuevo_usuario():
    return metodos.obtener_datos_de_registro()

if __name__ == '__main__':
    app.run()
