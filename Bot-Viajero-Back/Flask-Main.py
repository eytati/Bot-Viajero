from flask import Response
from flask import abort, jsonify
from flask import json
from Modulos_propios import Method_Person, Method_Register_Route, Method_Routes
from flask import Flask
from flask.ext.pymongo import PyMongo
from flask_httpauth import  HTTPBasicAuth
from flask_cors import CORS

#--------------------------------------------Inicio del codigo---------------------------------------------------------#
app = Flask(__name__)
CORS(app)
#--------------------------------------------Para utilizar la autenticacion--------------------------------------------#
registro_auth = HTTPBasicAuth()

#------------------------------------------Conexion con la base de datos-----------------------------------------------#
app.config['MONGO_DBNAME']= 'botviajero'
app.config['MONGO_URI'] = 'mongodb://botViajero:bot5917@ds135800.mlab.com:35800/botviajero'
app.config.from_object(__name__)
base_de_datos = PyMongo(app)

#----------------------------------Instancia de la clase de los metodos de persona-------------------------------------#
instance_method_person = Method_Person.Conexion_con_datos()
instance_method_register_route = Method_Register_Route.Register_routes()


#--------------------------------------------Prueba de requerimiento de usuario----------------------------------------#
@app.route('/hola', methods=["GET",'POST'])
@registro_auth.login_required
def hola():
    return "Hola"

#---------------------------------------------Registro en la base de datos---------------------------------------------#
@app.route('/api/registrar/persona', methods = ['POST'])
def create_user():
    print('saludo')
    return instance_method_person.create_user(base_de_datos)

#------------------------------------------------Inicio de sesion------------------------------------------------------#
@app.route('/api/token/<user>', methods = ['GET'])
@registro_auth.login_required
def token(user):
    value = instance_method_person.generate_token(base_de_datos, user, 800)

    return Response(json.dumps(value), status=200)

@registro_auth.verify_password
def verify_password(user_token, password):
    respuesta = instance_method_person.authentication(base_de_datos, user_token, password)
    if not respuesta is True:
        valor = instance_method_person.verify_token(base_de_datos, user_token)
        if valor is True:
            return user_token
        return abort(400)
    return user_token

#------------------------------------------------Registro de rutas-----------------------------------------------------#

@app.route('/api/registrar/ruta/avion', methods=['Post'])
def registrar_plane():
    return instance_method_register_route.register_plane(base_de_datos)

@app.route('/api/registrar/ruta/taxi', methods=['Post'])
def registrar_taxi():
    return instance_method_register_route.register_taxi(base_de_datos)

@app.route('/api/registrar/ruta/tren', methods=['Post'])
def registrar_train():
    return instance_method_register_route.register_train(base_de_datos)

@app.route('/api/registrar/ruta/bus', methods=['Post'])
def registrar_bus():
    return instance_method_register_route.register_bus(base_de_datos)

if __name__ == '__main__':
    app.run(host= '192.168.1.137', port=5016)

