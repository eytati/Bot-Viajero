from flask import Response
from flask import json
from flask import jsonify
from flask import request


from Modulos_propios import Method_Transport, Sort_Json

from  Modulos_propios import Graph
class Use_graph:
    graph_information = Graph.create_graph()
    method_transport = Method_Transport.Register_transport()
    sort_data = Sort_Json.Sort()

    def load_nodes(self, string_connect):
        collections_nodes = string_connect.db.Ciudades

        for cities  in collections_nodes.find():
            city = cities['ciudad']
            self.graph_information.create_node(city, cities)
        return  "Correcto"

    def load_edges(self, string_connect):
        collections_routes = string_connect.db.Rutas
        for paths in collections_routes.find():
            origin = paths["a"]
            destination = paths["b"]
            weight = paths["weight"]
            self.graph_information.create_edge(origin, destination, weight)
        return "Correcto"
#---------------------------------------------Lista de lugares---------------------------------------------------------#
    def list_places(self):
        return jsonify({"Ciudades": self.graph_information.show_cities()})

#---------------------------------------------------Ruta mas corta-----------------------------------------------------#
    def short_path(self):
        origin = request.json.get('origin')
        destination = request.json.get('destination')
        if origin is None or destination is None:
            return jsonify({"Error": "Faltan datos"})
        return jsonify({"City": self.graph_information.show_short_path(origin, destination)})

#--------------------------Mejores rutas segun el medio de transporte--------------------------------------------------#
    def route_between_points(self, string_connect):
        origin = request.json.get('origin')
        destination = request.json.get('destination')
        if origin is None or destination is None:
            return jsonify({"Error": "Faltan datos"})
        best_transports =[]
        json_plane = self.best_plane(string_connect, origin, destination)
        best_transports.append(json_plane)
        json_taxi = self.best_taxi(string_connect, origin, destination)
        best_transports.append(json_taxi)
        json_bus = self.best_bus(string_connect, origin, destination)
        best_transports.append(json_bus)
        json_train = self.best_train(string_connect, origin, destination)
        best_transports.append(json_train)
        #data= json.dumps({"Rutas":[{json_plane},{json_bus},{json_taxi},{json_train}]})
        return jsonify({"Valores": str(best_transports)})
    def best_plane(self, string_connect, point_a, point_b):
#---------------------------------------------------Mejor ruta de avion-------------------------------------------------#
        best_path = self.graph_information.show_routes(point_a, point_b)
        if not best_path is False:
            data = self.method_transport.best_price_transport(string_connect, point_a, point_b, 'plane')
            if not data is False:
                 price = data['total']
                 path = data['path']
                 km= self.distance(point_a, point_b, path)

#---------------------El avion se utiliza aproximadamente la tercea parte de los kilometros que por tierra-------------#
                 km_plane = km - ((km + 1) / 3)

#-----------------------Calculo de tiempo que utiliza la formula v=(d/t) que se despeja t=(d/v)------------------------#
                 time_plane = data['time']
                 return  {"Transport": "plane","Precio": price, "Distancia": km_plane, "Duracion": time_plane}
        return  {"No disponible"}

    def best_taxi(self, string_connect, point_a, point_b):
#--------------------------------------------------Mejor ruta de avion-------------------------------------------------#
        best_path = self.graph_information.show_routes(point_a, point_b)

        if not best_path is False:

            data = self.method_transport.best_price_transport(string_connect, point_a, point_b, 'taxi')

            if not data is False:
                path = int(data['path'])
                km_taxi = self.distance(point_a, point_b, path)
                price_num = data['total_km']
                price = km_taxi * float(int(price_num))
                time = data['time']
                return {"Transport": "taxi","Precio": price, "Distancia": km_taxi, "Duracion": time}

        return {"No disponible"}

    def best_bus(self, string_connect, point_a, point_b):
        best_path = self.graph_information.show_routes(point_a, point_b)
        if not best_path is False:

            data = self.method_transport.best_price_transport(string_connect, point_a, point_b, 'bus')
            if not data is False:
                path = int(data['path'])
                km = self.distance(point_a, point_b,path)
                price = data['total']
                time_bus = data['time']
                return {"Transport": "bus","Precio": price, "Distancia": km, "Duracion": time_bus}

        return {"No disponible"}

    def best_train(self, string_connect, point_a, point_b):

        best_path = self.graph_information.show_routes(point_a, point_b)
        if not best_path is False:
            price = self.method_transport.best_price_transport(string_connect, point_a, point_b, 'tren')
            if not price is False:
                price = price['total']
                path = int(price['path'])
                km_train = self.distance(point_a, point_b, path)
                time_train = price['time']
                return {"Transport": "train", "Precio": price, "Distancia": km_train, "Duracion": time_train, "Camino": str(path)}
        return {"No disponible"}


    def best_cost(self, string_connection):

        arrival = request.json.get('origin')
        departure = request.json.get('destination')
        if arrival is None or departure is None:
            return jsonify({"Error": "Faltan datos"})
        array_cost = self.method_transport.transport_data(string_connection, arrival, departure)
        sort_array = self.sort_data.sort_list(array_cost, 'total')
        best =[]
        for counter in range(0, 5):
            if counter <= len(sort_array):
                path = sort_array[counter].get('path')
                distance = self.distance(arrival, departure, path)

                json = {
                    "origin": sort_array[counter].get('origin'),
                    "destination": sort_array[counter].get('destination'),
                    "company": sort_array[counter].get('company'),
                    "distance": distance,
                    "costo": sort_array[counter].get('total'),
                    "time": sort_array[counter].get('time')}
                best.append(json)
            else:
                best.append({"No disponible"})

        return jsonify(str(best))

    def better_time(self, string_connection):

        arrival = request.json.get('origin')
        departure = request.json.get('destination')
        if arrival is None or departure is None:
            return jsonify({"Error": "Faltan datos"})

        array_time = self.method_transport.transport_data(string_connection, arrival, departure)
        sort_array = self.sort_data.sort_list(array_time, 'time')
        best = {}

        for counter in range(0, 5):
            if counter <= len(sort_array):
                path = sort_array[counter].get('path')
                distance = self.distance(arrival, departure, path)

                json = {
                    "origin": sort_array[counter].get('origin'),
                    "destination": sort_array[counter].get('destination'),
                    "company": sort_array[counter].get('company'),
                    "distance": distance,
                    "costo": sort_array[counter].get('total'),
                    "time": sort_array[counter].get('time')}
                best=(json)
            else:
                best=({"No disponible"})
        return jsonify(str(best))

    def better_distance(self, string_connection):
        arrival = request.json.get('origin')
        departure = request.json.get('destination')
        if arrival is None or departure is None:
            return jsonify({"Error": "Faltan datos"})

        array_all_routes = self.graph_information.show_all_routes(arrival, departure)

        if not array_all_routes is False:
            sort_array = self.sort_data.sort_list(array_all_routes, 'Distancia')
            transport_array = self.method_transport.transport_data(string_connection, arrival, departure)
            datos =self.sort_distance_data(sort_array, transport_array)

            return  jsonify({"Rutas": str(datos)})
        return jsonify({"Estado": "No hay rutas"})


    def sort_distance_data(self, sort_array, transport_array):
        best = []
        while len(best) <= 4:
            for counter in range(len(sort_array)):
                number = sort_array[counter].get('Numero de ruta')
                for counter_transport in range(len(transport_array)):
                    valor =  transport_array[counter_transport].get('path')
                    if number == valor:
                        json = {
                            "origin": transport_array[counter_transport].get('origin'),
                            "destination":transport_array[counter_transport].get('destination'),
                            "company": transport_array[counter_transport].get('company'),
                            "distance": sort_array[counter].get('Distancia'),
                            "costo": transport_array[counter_transport].get('total'),
                            "time": transport_array[counter_transport].get('time')
                        }
                        best.append(json)
            if len(best) <=4 :
                best.append({"No disponible"})
        return best

#------------------------------------------Obtener km de distancia-----------------------------------------------------#
    def distance(self, arrival, departure, path):
        array_all_routes = self.graph_information.show_all_routes(arrival, departure)
        for counter in range(len(array_all_routes)):
            number = array_all_routes[counter].get('Numero de ruta')
            if number == path:
                return int(array_all_routes[counter].get('Distancia'))
        return 0

