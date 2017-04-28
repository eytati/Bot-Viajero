from datetime import datetime

from flask import Response
from flask import abort, jsonify
from flask import json
from flask import request
import logging
from logging.handlers import RotatingFileHandler

from numpy import unicode

from Modulos_propios import Method_Person, Method_Transport, Method_Routes
from flask import Flask
from flask.ext.pymongo import PyMongo
from flask_httpauth import  HTTPBasicAuth
from flask_cors import CORS

#--------------------------------------------Inicio del codigo---------------------------------------------------------#
app = Flask(__name__)
logging.getLogger(__name__)
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

#-------------------------------------Carga el grafo antes del servicio------------------------------------------------#
with app.app_context():
    print(instance_method_routes.load_nodes(base_de_datos))
    print(instance_method_routes.load_edges(base_de_datos))


#--------------------------------------------Si hace un request a una ruta desconocida---------------------------------#
@app.before_request
def verifiqueRutas():
    uri = request.url_rule
    if uri == None:
        rquest = request.environ['REMOTE_ADDR']
        logger("Intento acceder a ruta desconocida", rquest)
        app.logger.info(str(datetime.now()) + "Intento acceder a ruta desconocida")
        return jsonify("Ruta desconocida")

#--------------------------------------------Prueba de requerimiento de usuario----------------------------------------#
@app.route('/api/ciudades', methods=["GET"])
def index():
    rquest  =  request.environ['REMOTE_ADDR']
    logger('Se solicito ver las ciudades', rquest)
    return instance_method_routes.list_places()

#-------------------------------------------------Rutas mas corta------------------------------------------------------#
@app.route('/api/ruta/corta', methods=["POST"])
def short_route():
    rquest = request.environ['REMOTE_ADDR']
    logger('Se solicito ver las ciudades', rquest)
    app.logger.info(str(datetime.now()) + "Solicito ruta mas corta")
    return instance_method_routes.short_path()

#-----------------------------------------------------Rutas del grafo--------------------------------------------------#
@app.route('/api/rutas/mejores/transporte', methods=['POST'])
def best_routes():
    print('hola')
    rquest = request.environ['REMOTE_ADDR']
    logger("Mejor ruta segun el transporte", rquest)
    app.logger.info(str(datetime.now()) + "Mejor ruta segun el transporte")
    return instance_method_routes.route_between_points(base_de_datos)

@app.route('/api/rutas/mejores/costo', methods=['POST'])
def better_cost():
    print('hola')
    rquest = request.environ['REMOTE_ADDR']
    logger("Solicito las rutas mas corta en terminos de costo", rquest)
    app.logger.info(str(datetime.now()) + "Solicito las rutas mas corta en terminos de costo")
    return instance_method_routes.best_cost(base_de_datos)

@app.route('/api/rutas/mejores/tiempo', methods=['POST'])
def better_time():
    print('hola')
    rquest = request.environ['REMOTE_ADDR']
    logger("Solicito las rutas mas corta en terminos de tiempo", rquest)
    app.logger.info(str(datetime.now()) + "Solicito las rutas mas corta en terminos de tiempo")
    return instance_method_routes.better_time(base_de_datos)

@app.route('/api/rutas/mejores/distancia', methods=['POST'])
def better_distance():
    print('hola')
    rquest = request.environ['REMOTE_ADDR']
    logger("Solicito las rutas mas corta en terminos de distancia", rquest)
    app.logger.info(str(datetime.now()) + "Solicito las rutas mas corta en terminos de distancia")
    return instance_method_routes.better_distance(base_de_datos)


#---------------------------------------------Registro en la base de datos---------------------------------------------#
@app.route('/api/registrar/persona', methods = ['POST'])
def create_user():
    rquest = request.environ['REMOTE_ADDR']
    logger("Se registro nuevo usuario", rquest)
    app.logger.info(str(datetime.now()) + "Se registro nuevo usuario")
    return instance_method_person.create_user(base_de_datos)

#------------------------------------------------Inicio de sesion------------------------------------------------------#
@app.route('/api/token/<user>', methods = ['GET'])
@registro_auth.login_required
def token(user):
    value = instance_method_person.generate_token(base_de_datos, user, 800)
    rquest = request.environ['REMOTE_ADDR']
    logger("Solicito token, con el usuario "+user+" Obtuvo el token" +value, rquest)
    return Response(json.dumps(value), status=200)

@registro_auth.verify_password
def verify_password(user_token, password):
    print(user_token)
    print(password)
    rquest = request.environ['REMOTE_ADDR']
    respuesta = instance_method_person.authentication(base_de_datos, user_token, password)
    if not respuesta is True:
        valor = instance_method_person.verify_token(base_de_datos, user_token)
        if valor is True:
            logger("Solicito authenticacion con" + user_token , rquest)
            app.logger.info(str(datetime.now()) + "Se autentico como" + user_token)
            return user_token
        logger("Solicito authenticacion " + user_token+ "ACCESO DENEGADO", rquest,)
        app.logger.info(str(datetime.now()) + "Se denego acceso" + user_token)
        return abort(400)
    logger("Solicito authenticacion " + user_token, rquest)
    app.logger.info(str(datetime.now()) + "Se autentico como" + user_token)
    return user_token

#------------------------------------------------Registro de rutas-----------------------------------------------------#

@app.route('/api/registrar/ruta/avion', methods=['Post'])
@registro_auth.login_required
def registrar_plane():
    rquest = request.environ['REMOTE_ADDR']
    logger("Registro una ruta de avion", rquest)
    app.logger.info(str(datetime.now()) + 'Registro una ruta de avion')
    return instance_method_transport.register_plane(base_de_datos)

@app.route('/api/registrar/ruta/taxi', methods=['Post'])
@registro_auth.login_required
def registrar_taxi():
    rquest = request.environ['REMOTE_ADDR']
    logger("Registro una ruta de taxi", rquest)
    app.logger.info(str(datetime.now()) + 'Registro una ruta de taxi')
    return instance_method_transport.register_taxi(base_de_datos)

@app.route('/api/registrar/ruta/tren', methods=['Post'])
@registro_auth.login_required
def registrar_train():
    rquest = request.environ['REMOTE_ADDR']
    logger("Registro una ruta de tren", rquest)
    app.logger.info(str(datetime.now()) + 'Registro una ruta de tren')
    return instance_method_transport.register_train(base_de_datos)

@app.route('/api/registrar/ruta/bus', methods=['Post'])
@registro_auth.login_required
def registrar_bus():
    rquest = request['REMOTE_ADDR']
    logger("Registro una ruta de bus", rquest)
    app.logger.info(str(datetime.now()) + 'Registro una ruta de bus')
    return instance_method_transport.register_bus(base_de_datos)

def logger(do, person):
        collection_logger = base_de_datos.db.Logger
        now = datetime.now()
        now_date = unicode(now.replace(microsecond=0))
        collection_logger.insert({"Hizo una solicitud de": do, "El dia y la hora": now_date, "Solicitud de request desde": person})

if __name__ == '__main__':
    handler = RotatingFileHandler('tati-bot.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host= '192.168.1.138', port=5016)

