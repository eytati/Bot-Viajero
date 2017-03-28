from flask import Flask, jsonify, request, abort
from Modulos import Usuario
from Modulos import Password_propia

app = Flask(__name__)

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

@app.route('/api/token')
#@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({ 'token': token.decode('ascii') })




if __name__ == '__main__':
    app.run()