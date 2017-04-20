from datetime import datetime

from flask import request, jsonify

class Register_transport():

#-----------------------------------------------Calculo de tiempo------------------------------------------------------#
    def time(self, arrival_time, departure_time):
        format = "%H:%M:%S"
        hour_1 = datetime.strptime(arrival_time, format)
        hour_2 = datetime.strptime(departure_time, format)
        time = hour_2 - hour_1
        return str(time)

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
            return jsonify({"Error": "Faltan datos"})

        if destination is None or passengers is None or departure_time is None:
            return jsonify({"Error": "Faltan datos"})

        if arrival_time is None or total is None:
            return jsonify({"Error": "Faltan datos"})

#-----------------------------------------Valores del json de las rutas------------------------------------------------#

        time = self.time(arrival_time,departure_time)

        json_edges_db = {"type": "plane",
                         "company": company,
                         "origin": origin,
                         "destination" : destination,
                         "passengers": passengers,
                         "departure_time": departure_time,
                         "arrival_time" : arrival_time,
                         "time": time,
                         "total": total
                         }

#---------------------------Conexion con las bases de datos y ingresar la ruta-----------------------------------------#

        collection_transport =string_connection.db.Transportes
        collection_transport.insert(json_edges_db)
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
            return jsonify({"Error": "Faltan datos"})

        if destination is None or departure_time is None:
            return jsonify({"Error": "Faltan datos"})

        if arrival_time is None or total is None:
            return jsonify({"Error": "Faltan datos"})

#-----------------------------------------Valores del json de las rutas------------------------------------------------#

        time = self.time(arrival_time, departure_time)

        json_edges_db = {
            "type": "train",
            "company": company,
            "origin": origin,
            "destination": destination,
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "time": time,
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
        last_name= request.json.get('lastname')
        origin = request.json.get('origin')
        destination = request.json.get('destination')
        departure_time = request.json.get('departure_time')
        arrival_time = request.json.get('arrival_time')
        total = request.json.get('total')

#-----------------------------------------------Revision de datos------------------------------------------------------#
        if company is None or registration is None or origin is None:
            return jsonify({"Error": "Faltan datos"})

        if destination is None or id is None or departure_time is None:
            return jsonify({"Error": "Faltan datos"})

        if name is None or last_name is None:
            return jsonify({"Error": "Faltan datos"})

        if arrival_time is None or total is None:
            return jsonify({"Error": "Faltan datos"})

#-----------------------------------------Valores del json de las rutas------------------------------------------------#

        time = self.time(arrival_time, departure_time)

        json_edges_db = {
            "type": "taxi",
            "registration": registration,
            "id": id,
            "name":  name,
            "lastname": last_name,
            "company": company,
            "origin": origin,
            "destination": destination,
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "time": time,
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
            return jsonify({"Error": "Faltan datos"})

        if destination is None or departure_time is None:
            return jsonify({"Error": "Faltan datos"})

        if name is None or passengers is None:
            return jsonify({"Error": "Faltan datos"})

        if arrival_time is None or total is None:
            return jsonify({"Error": "Faltan datos"})

#-----------------------------------------Valores del json de las rutas------------------------------------------------#

        time = self.time(arrival_time, departure_time)

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
            "time": time,
            "total": total}

#---------------------------Conexion con las bases de datos y ingresar la ruta-----------------------------------------#
        collection_transport = string_connection.db.Transportes
        collection_transport.insert(json_edges_db)
        return jsonify({"Estado": "Se agrego correctamente", "Datos": str(json_edges_db)})


#-----------------------------------------Mejor precio por tipo de transporte------------------------------------------#
    def best_price_transport(self, string_connection, point_a, point_b, transport):
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
                    best_price = data['total']
                    if best_price > data['total']:
                        best = data
        if best == {}:
            return False
        return best

#-----------------------------------------rutas disponibles------------------------------------------------------------#
    def best_price(self, string_connection, arrival, departure):
     collection_transport = string_connection.db.Transportes
     options= []
     for data in collection_transport.find():
         origin= data['origin']
         destination = data['destination']
         if origin == arrival and destination == departure:
             options.append(data)
     if options is []:
         return False
     return options

#------------------------------------------agragar tiempo--------------------------------------------------------------#






