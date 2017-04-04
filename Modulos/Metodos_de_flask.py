from Modulos import  Usuario, Password_propia
from flask import request, abort, jsonify

class Metodos_requeridos():
    def obtener_datos_de_registro(self):
        usuario = Usuario.usuario()
        username = request.json.get('username')
        password = request.json.get('password')
        repassword = request.json.get('repassword')

        if username is None or password is None:  #
            abort(400)
            return "Faltan Datos"
        if usuario.verificar_usuario(username):
            abort(400)
            return 'Ya existe un usuario'
        if not password == repassword:
            abort(400)
            return 'Las contraseñas no coinciden'
        contrasena = Password_propia.feature_password()
        password = contrasena.hash_password(password)
        usuario.agregar(username, password)

        return jsonify({'username': username}), 201  # {'Location': url_for('get_user', id = user.id, _external = True)}