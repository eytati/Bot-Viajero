from flask import Response
from flask import abort, jsonify
from flask import json
from flask import request
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature)
from Modulos_propios import Method_Persona
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

#----------------------------------Instancia de la clase de los metodos de flask---------------------------------------#
intance_method_flask = Method_Persona.Conexion_con_datos()

@app.route('/hola', methods=["GET",'POST'])
@registro_auth.login_required
def hola():
    return "Hola"

#---------------------------------------------Registro en la base de datos---------------------------------------------#
@app.route('/api/registrar/persona', methods = ['POST'])
def create_user():
    print('saludo')
    return intance_method_flask.create_user(base_de_datos)

#------------------------------------------------Inicio de sesion------------------------------------------------------#
@app.route('/api/token/<user>', methods = ['GET'])
@registro_auth.login_required
def token(user):
    value = intance_method_flask.generate_token(base_de_datos, user, 800)

    return Response(json.dumps(value), status=200)

@registro_auth.verify_password
def verify_password(user_token, password):
    respuesta = intance_method_flask.authentication(base_de_datos, user_token, password)
    if not respuesta is True:
        valor = intance_method_flask.verify_token(base_de_datos, user_token)
        if valor is True:
            return user_token
        return abort(400)
    return user_token

if __name__ == '__main__':
    app.run(host= '192.168.1.137', port=5016)
