from flask import jsonify

from  Modulos_propios import Graph
class Use_graph:
    graph_information = Graph.create_graph()

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
        #Mejor ruta en avion
        best_path = self.graph_information.show_routes('Tortuguero', 'Liberia')
        #Mejor precio
        return jsonify({"Estado": "Sirve"})

    #Mejor ruta en tren
    #Mejor ruta en bus
    #Mejor ruta en taxi

        #return

    def best_distance(self):
        return

    def best_cost(self):
        return

