from flask import request, jsonify

class Register_transport():

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

        print("hola 2")

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

        collection_transport =string_connection.db.Transportes
        collection_transport.insert(json_edges_db)
        print("HOlA")
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
        collection_transport = string_connection.db.Transportes
        collection_transport.insert(json_edges_db)
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
        collection_transport = string_connection.db.Transportes
        collection_transport.insert(json_edges_db)
        return jsonify({"Estado": "Se agrego correctamente", "Datos": str(json_edges_db)})

#--------------------------------------------------------Registrar bus--------------------------------------------------------------------------------#
    def register_bus(self, string_connection):
#-----------------------------------------------Obtiene datos----------------------------------------------------------#
        companymame = request.json.get('companyname')
        registration = request.json.get('registration')
        name = request.json.get('name')
        passengers = request.json.get('passengers')
        origin = request.json.get('origin')
        destination = request.json.get('destination')
        departure_time = request.json.get('departure_time')
        arrival_time = request.json.get('arrival_time')
        total = request.json.get('total')

#-----------------------------------------------Revision de datos------------------------------------------------------#
        if companymame is None or registration is None or origin is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

        if destination is None or departure_time is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})

        if name is None or passengers is None:
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
            'name': name,
            'passengers': passengers,
            "company": companymame,
            "origin": origin,
            "destination": destination,
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "total": total}

#---------------------------Conexion con las bases de datos y ingresar la ruta-----------------------------------------#
        collection_transport = string_connection.db.Transportes
        collection_transport.insert(json_edges_db)
        return jsonify({"Estado": "Se agrego correctamente", "Datos": str(json_edges_db)})


#-----------------------------------------Mejor precio por tipo de transporte------------------------------------------#
    def best_price(self, string_connection, point_a, point_b, transport):
        collection_transport = string_connection.db.Transportes
        best = {}
        for data in collection_transport.find():
            origin = data['origin']
            destination = data['destination']
            if origin == point_a and destination == point_b:
                if data['type'] == transport:
                    if best == {}:
                        best = data
                else:
                    best_price = best['total']
                    if best_price > data['total']:
                        best = data
        if best == {}:
            return False
        return best
