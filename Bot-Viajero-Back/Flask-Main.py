from flask import Response
from flask import abort, jsonify
from flask import json
from flask import request

from Modulos_propios import Method_Person, Method_Transport, Method_Routes
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
instance_method_transport = Method_Transport.Register_transport()
instance_method_routes = Method_Routes.Use_graph()

@app.before_request
def verifiqueRutas():
    uri = request.url_rule
    if uri == None:
        return jsonify("Ruta desconocida")
#--------------------------------------------Prueba de requerimiento de usuario----------------------------------------#
@app.route('/api/ciudades', methods=["GET"])
def index():
    return instance_method_routes.list_places()

#-----------------------------------------------------Rutas del grafo--------------------------------------------------#
@app.route('/api/rutas/mejores/transporte', methods=['POST'])
def best_routes():
    print('hola')
    instance_method_routes.load_nodes(base_de_datos)
    instance_method_routes.load_edges(base_de_datos)
    return instance_method_routes.route_between_points(base_de_datos)

@app.route('/api/rutas/mejores/costo', methods=['POST'])
def better_cost():
    print('hola')
    return instance_method_routes.best_cost(base_de_datos)

@app.route('/api/rutas/mejores/tiempo', methods=['POST'])
def better_time():
    print('hola')
    return instance_method_routes.better_time(base_de_datos)

@app.route('/api/rutas/mejores/distancia', methods=['POST'])
def better_distance():
    print('hola')
    return instance_method_routes.better_distance(base_de_datos)


#---------------------------------------------Registro en la base de datos---------------------------------------------#
@app.route('/api/registrar/persona', methods = ['POST'])
def create_user():
    return instance_method_person.create_user(base_de_datos)

#------------------------------------------------Inicio de sesion------------------------------------------------------#
@app.route('/api/token/<user>', methods = ['GET'])
@registro_auth.login_required
def token(user):
    value = instance_method_person.generate_token(base_de_datos, user, 800)

    return Response(json.dumps(value), status=200)

@registro_auth.verify_password
def verify_password(user_token, password):
    print(user_token)
    print(password)
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
    return instance_method_transport.register_plane(base_de_datos)

@app.route('/api/registrar/ruta/taxi', methods=['Post'])
def registrar_taxi():
    return instance_method_transport.register_taxi(base_de_datos)

@app.route('/api/registrar/ruta/tren', methods=['Post'])
def registrar_train():
    return instance_method_transport.register_train(base_de_datos)

@app.route('/api/registrar/ruta/bus', methods=['Post'])
def registrar_bus():
    return instance_method_transport.register_bus(base_de_datos)

if __name__ == '__main__':
    app.run(host= '192.168.1.138', port=5016)

