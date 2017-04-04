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
    if username is None or password is None:#
        abort(400)
        return "Faltan Datos"
    if usuario.verificar_usuario(username):
        abort(400)
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

@app.route('/api/login/persona', methods = ['GET'])
@registro_auth.verify_password
def revision_de_datos(user, passw):
    usuario =  Usuario.usuario()
    usuario_prueba = usuario.verificar_usuario_pass(user, passw)
    if not usuario_prueba:
        abort(400)
    token = usuario.generate_auth_token(usuario, expiration=700)
    return jsonify({'token': token.decode('ascii')})






'''
@app.route('/api/login/persona', methods = ['POST'])
def revision_de_datos():
    username = request.json.get('username')
    password = request.json.get('password')
    usuario =  Usuario.usuario()
    usuario_prueba = usuario.verificar_usuario_pass(username, password)
    if not usuario_prueba:
        abort(400)
    token = usuario.generate_auth_token(usuario, expiration=700)
    return jsonify({'token': token.decode('ascii')})
'''
if __name__ == '__main__':
    app.run()