from flask import jsonify

from  Modulos_propios import Graph
class Use_graph:

    graph_information = Graph.create_graph()

    def list_places(self):
        return jsonify({"Ciudades": self.graph_information.show_cities()})

    def route_between_points(self):
        return

    def best_distance(self):
        return

    def best_time(self):
        return

    def best_cost(self):
        return

