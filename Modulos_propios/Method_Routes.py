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
            print(str(city))
            self.graph_information.create_node(city, cities)
        return  jsonify({"Estago": "Se agrego correctamente"})

    def load_edges(self, string_connect):
        collections_routes = string_connect.db.Rutas
        for paths in collections_routes.find():
            origin = paths["a"]
            destination = paths["b"]
            weight = paths["weight"]
            self.graph_information.create_edge(origin, destination, weight)
        return jsonify({"Estago": "Se agrego correctamente"})

    def list_places(self):
        return jsonify({"Ciudades": self.graph_information.show_cities()})

    def route_between_points(self, string_connect):
        origin = request.json.get('origin')
        destination = request.json.get('destination')
        if origin is None or destination is None:
            # abort(400)
            print("Faltan Datos")
            return jsonify({"Error": "Faltan datos"})
        best_transports = []
        json_plane = self.best_plane(string_connect, origin, destination)
        best_transports.append(json_plane)
        json_taxi = self.best_taxi(string_connect, origin, destination)
        best_transports.append(json_taxi)
        json_bus = self.best_bus(string_connect, origin, destination)
        best_transports.append(json_bus)
        json_train = self.best_train(string_connect, origin, destination)
        best_transports.append(json_train)

        return jsonify({"Datos": str(best_transports)})

    def best_plane(self, string_connect, point_a, point_b):
#---------------------------------------------------Mejor ruta de avion-------------------------------------------------#
        best_path = self.graph_information.show_routes(point_a, point_b)
        if not best_path is False:
            path = best_path['Camino']
            km = best_path['Total de Km']
            price = self.method_transport.best_price_transport(string_connect, point_a, point_b, 'plane')
            if not price is False:
                 price = price['total']
#---------------------El avion se utiliza aproximadamente la tercea parte de los kilometros que por tierra-------------#
                 km_plane = km - ((km + 1) / 3)
#-----------------------Calculo de tiempo que utiliza la formula v=(d/t) que se despeja t=(d/v)------------------------#
                 time_plane = (km_plane / 97)
                 return  {"Precio": price, "Distancia": km_plane, "Duracion": time_plane, "Camino": str(path)}
        return  {"No disponible"}

    def best_taxi(self, string_connect, point_a, point_b):
#--------------------------------------------------Mejor ruta de avion-------------------------------------------------#
        best_path = self.graph_information.show_routes(point_a, point_b)

        if not best_path is False:
            path = best_path['Camino']
            km = best_path['Total de Km']
            price = self.method_transport.best_price_transport(string_connect, point_a, point_b, 'taxi')

            if not price is False:
                km_taxi = km - ((km ) / 20) #El taxi se  disminuye la vigesima parte de los kilometros por las variaciones en rutas
                price_num =price['total']
                price = km_taxi * int(price_num)
                time_taxi = (km_taxi / 50)#Calculo de tiempo que utiliza la formula v=(d/t) que se despeja t=(d/v)
                return {"Precio": price, "Distancia": km_taxi, "Duracion": time_taxi, "Camino": str(path)}

        return {"No disponible"}

    def best_bus(self, string_connect, point_a, point_b):

        best_path = self.graph_information.show_routes(point_a, point_b)
        if not best_path is False:
            path = best_path['Camino']
            km = best_path['Total de Km']
            price = self.method_transport.best_price_transport(string_connect, point_a, point_b, 'bus')
            if not price is False:
                price = price['total']
                time_bus = (km / 30) #
                return {"Precio": price, "Distancia": km, "Duracion": time_bus, "Camino": str(path)}

        return {"No disponible"}

    def best_train(self, string_connect, point_a, point_b):

        best_path = self.graph_information.show_routes(point_a, point_b)
        if not best_path is False:
            path = best_path['Camino']
            km = best_path['Total de Km']
            price = self.method_transport.best_price_transport(string_connect, point_a, point_b, 'tren')

            if not price is False:
                price = price['total']
                km_train = km-(km*0.03)#Se disminuye un 3% ela cantidad de kilometros
                time_train = (km_train / 40)#Calculo de tiempo que utiliza la formula v=(d/t) que se despeja t=(d/v)
                return {"Precio": price, "Distancia": km_train, "Duracion": time_train, "Camino": str(path)}

        return {"No disponible"}

    def best_time(self, string_connection):
        arrival = request.json.get('origin')
        departure = request.json.get('destination')
        if arrival is None or departure is None:
            return jsonify({"Error": "Faltan datos"})


        return

    def best_cost(self, string_connection):
        arrival = request.json.get('origin')
        departure = request.json.get('destination')
        if arrival is None or departure is None:
            return jsonify({"Error": "Faltan datos"})
        array_cost = self.method_transport.best_price(string_connection, arrival,departure)
        best = self.sort_data.sort_list(array_cost, 'total')

        return jsonify(str(best))

