from flask import request, jsonify
from  Modulos_propios import Graph

class Load_data():
#-------------------------------------------Cargar Rutas de la base de Datos-------------------------------------------#
    def load_data_edges(self, string_connection):
        collection_routes = string_connection.db.Rutas
        for counter in collection_routes.find():
            self.load_one(counter)
        return jsonify({"Estado": "Se agrego a la base de datos"})

#-------------------------------------------Cargar Rutas de la base de Datos-------------------------------------------#
    def load_data_nodes(self, string_connection):
        collection_cities = string_connection.db.Ciudades
        load_graph = Graph.create_graph()
        for counter in collection_cities.find():
            name = counter['ciudad']
            load_graph.create_node(name, counter)
            print(" ciudad: " + name + "json" + str(counter))
        return jsonify({"Estado": "Se agrego a grafo"})

#------------------------------------------------Cargar una arista-----------------------------------------------------#
    def load_one(self,valor):
        load_graph = Graph.create_graph()
        origin = valor['origin']
        destination = valor['destination']
        load_graph.create_edge(origin, destination, valor)
        print("origin: " + origin + " destination: " + destination + "json" + str(valor))
        return jsonify({"Estado":"Se realiza correctamente", "\nDatos":str(valor)})


class Register_routes():

    instance_load = Load_data()
#--------------------------------------------------------Registrar avion--------------------------------------------------------------------------------#
    def register_plane(self, string_connection):
#-----------------------------------------------Obtiene datos----------------------------------------------------------#
        company = request.json.get('company')
        origin = request.json.get('origin')
        destination = request.json.get('destination')
        passengers= request.json.get('passengers')
        departure_time= request.json.get('departure_time')
        arrival_time = request.json.get('arrival_time')
        total = request.json.get('total')

#-----------------------------------------------Revision de datos------------------------------------------------------#
        if company is None or origin is None:
            # abort(400)
            print("Faltan Datos1")
            return jsonify({"Error": "Faltan datos 1"})

        if destination is None or passengers is None or departure_time is None:
            # abort(400)
            print("Faltan Datos2")
            return jsonify({"Error": "Faltan datos 2"})

        if arrival_time is None or total is None:
            # abort(400)
            print("Faltan Datos3")
            return jsonify({"Error": "Faltan datos 3"})

#-----------------------------------------Valores del json de las rutas------------------------------------------------#
        json_edges_db = {"type": "plane",
                         "company": company,
                         "origin": origin,
                         "destination" : destination,
                         "passangers": passengers,
                         "departure_time": departure_time,
                         "arrival_time" : arrival_time,
                         "total": total}

#---------------------------Conexion con las bases de datos y ingresar la ruta-----------------------------------------#
        collection_routes =string_connection.db.Rutas
        collection_routes.insert(json_edges_db)
        self.instance_load.load_one(json_edges_db)
        return jsonify({"Estado": "Se agrego correctamente", "Datos": str(json_edges_db)})

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
        self.instance_load.load_one(json_edges_db)
        return jsonify({"Estado": "Se agrego correctamente", "Datos": str(json_edges_db)})

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
        self.instance_load.load_one(json_edges_db)
        return jsonify({"Estado": "Se agrego correctamente", "Datos": str(json_edges_db)})

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
        self.instance_load.load_one(json_edges_db)
        return jsonify({"Estado": "Se agrego correctamente", "Datos": str(json_edges_db)})



