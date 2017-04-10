from flask import Response
from flask import request, jsonify
from  Modulos_propios import Graph

class Register_routes():

#--------------------------------------------------------Registrar avion--------------------------------------------------------------------------------#
    def register_plane(self, string_connection):
#-----------------------------------------------Obtiene datos----------------------------------------------------------#
        company = request.json.get('company')
        origin = request.json.get('origin')
        destination = request.json.get('destination')
        passangers= request.json.get('passangers')
        departure_time= request.json.get('departure_time')
        arrival_time = request.json.get('arrival_time')
        total = request.json.get('total')

#-----------------------------------------------Revision de datos------------------------------------------------------#
        if company is None or origin is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

        if destination is None or passangers is None or departure_time is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

        if arrival_time is None or total is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

#-----------------------------------------Valores del json de las rutas------------------------------------------------#
        json_edges_db = {"type": "plane", "company": company, "origin": origin, "destination" : destination,"passangers": passangers, "departure_time": departure_time, "arrival_time" : arrival_time, "total": total}

#---------------------------Conexion con las bases de datos y ingresar la ruta-----------------------------------------#
        collection_routes =string_connection.db.Rutas
        collection_routes.insert(json_edges_db)
        return jsonify({"Estado": "Se agrego correctamente"})


#--------------------------------------------------------Registrar Tren--------------------------------------------------------------------------------#
    def register_train(self, string_connection):
#-----------------------------------------------Obtiene datos----------------------------------------------------------#
        company = request.json.get('company')
        origin = request.json.get('origin')
        destination = request.json.get('destination')
        departure_time = request.json.get('departure_time')
        arrival_time = request.json.get('arrival_time')
        total = request.json.get('total')

#-----------------------------------------------Revision de datos------------------------------------------------------#
        if company is None or origin is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

        if destination is None or departure_time is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

        if arrival_time is None or total is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

#-----------------------------------------Valores del json de las rutas------------------------------------------------#
        json_edges_db = {
            "type": "train",
            "company": company,
            "origin": origin,
            "destination": destination,
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "total": total}

#---------------------------Conexion con las bases de datos y ingresar la ruta-----------------------------------------#
        collection_routes = string_connection.db.Rutas
        collection_routes.insert(json_edges_db)

        return jsonify({"Estado": "Se agrego correctamente"})

#--------------------------------------------------------Registrar Taxi--------------------------------------------------------------------------------#

    def register_taxi(self, string_connection):
#-----------------------------------------------Obtiene datos----------------------------------------------------------#
        company = request.json.get('company')
        registration = request.json.get('registration')
        id = request.json.get('id')
        name = request.json.get('name')
        lastname= request.json.get('lastname')
        origin = request.json.get('origin')
        destination = request.json.get('destination')
        departure_time = request.json.get('departure_time')
        arrival_time = request.json.get('arrival_time')
        total = request.json.get('total')

#-----------------------------------------------Revision de datos------------------------------------------------------#
        if company is None or registration is None or origin is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

        if destination is None or id is None or departure_time is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

        if name is None or lastname is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

        if arrival_time is None or total is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

#-----------------------------------------Valores del json de las rutas------------------------------------------------#
        json_edges_db = {
            "type": "taxi",
            "registration": registration,
            "id": id,
            "name":  name,
            "lastname": lastname,
            "company": company,
            "origin": origin,
            "destination": destination,
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "total": total}

#---------------------------Conexion con las bases de datos y ingresar la ruta-----------------------------------------#
        collection_routes = string_connection.db.Rutas
        collection_routes.insert(json_edges_db)

        return jsonify({"Estado": "Se agrego correctamente"})

#--------------------------------------------------------Registrar bus--------------------------------------------------------------------------------#
    def register_bus(self, string_connection):
#-----------------------------------------------Obtiene datos----------------------------------------------------------#
        company = request.json.get('company')
        registration = request.json.get('registration')
        id = request.json.get('id')
        name = request.json.get('name')
        passagers = request.json.get('passagers')
        origin = request.json.get('origin')
        destination = request.json.get('destination')
        departure_time = request.json.get('departure_time')
        arrival_time = request.json.get('arrival_time')
        total = request.json.get('total')

#-----------------------------------------------Revision de datos------------------------------------------------------#
        if company is None or registration is None or origin is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

        if destination is None or id is None or departure_time is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

        if name is None or passagers is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

        if arrival_time is None or total is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

#-----------------------------------------Valores del json de las rutas------------------------------------------------#
        json_edges_db = {
            "type": "bus",
            'registration': registration,
            'id': id,
            'name': name,
            'passagers': passagers,
            "company": company,
            "origin": origin,
            "destination": destination,
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "total": total}

#---------------------------Conexion con las bases de datos y ingresar la ruta-----------------------------------------#
        collection_routes = string_connection.db.Rutas
        collection_routes.insert(json_edges_db)

        return jsonify({'Estado': "Se agrego correctamente"})