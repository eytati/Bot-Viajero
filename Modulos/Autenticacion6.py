from flask import Flask, jsonify, request, abort
from Modulos import Usuario
from Modulos import Password_propia
from flask_httpauth import  HTTPBasicAuth

app = Flask(__name__)
registro_auth = HTTPBasicAuth()

@app.route('/api/registrar/persona', methods = ['POST'])
def nuevo_usuario():
    usuario = Usuario.usuario()
    username = request.json.get('username')
    password = request.json.get('password')
    repassword = request.json.get('repassword')
    if username is None or password is None:# or repassword is None:
        abort(400) # faltan datos
        return "Faltan Datos"
    if usuario.verificar_usuario(username):
        abort(400)#Existe usuario
        return 'Ya existe un usuario'
    if not password== repassword:
        abort(400)
        return 'Las contraseñas no coinciden'
    contrasena = Password_propia.feature_password()
    password= contrasena.hash_password(password)
    usuario.agregar(username, password)

    return jsonify({ 'username': username }), 201# {'Location': url_for('get_user', id = user.id, _external = True)}

@app.route('/api/resource')
@registro_auth.login_required
def get_resource():
    return jsonify({ 'Hello' })

@app.route('/api/login/persona', methods = ['POST'])
def revision_de_datos():
    username = request.json.get('username')
    password = request.json.get('password')
    usuario =  Usuario.usuario()
    contra =  Password_propia.feature_password()
    password_con_hash = contra.hash_password(password)
    usuario_prueba = usuario.verificar_usuario_pass(username, password_con_hash)
    if not usuario_prueba:
        abort(400)
    return "Su usuario es correcto"





@app.route('/api/token')
#@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({ 'token': token.decode('ascii') })




if __name__ == '__main__':
    app.run()