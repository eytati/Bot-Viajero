import networkx as nx
import json

from flask import jsonify


class create_graph:
    grafo = nx.Graph()
    instance = None

    def __init__(self):
        if not self.grafo.instance:
            self.grafo.instance = self

    def create_node(self, name, data_json):
        self.grafo.add_node(name, data_json)

    def create_edge(self, origin, destination, weight):
        self.grafo.add_edge(origin, destination, weight = weight)

    def show_cities(self):
        cities = []
        for couter in self.grafo.node:
            graph_data = self.grafo.node[couter]
            if not graph_data == {}:
                id = graph_data['id']
                city = graph_data['ciudad']
                latitude = graph_data['latitude']
                longitude = graph_data['longitude']
                json_data = {"Id": id, "Ciudad": city, "Latitud": latitude, "Longitud": longitude}
                cities.append(json_data)
        print(cities)
        return cities

    def show_routes(self, source, target):
        exists = nx.has_path(self.grafo,  source, target)
        if exists is True:
            path = []
            for value in nx.all_shortest_paths(self.grafo, source, target, weight='weight'):
                for a in range(len(value)):
                    data = value[a]
                    new_data = self.grafo.node[data]
                    id = new_data['id']
                    city = new_data['ciudad']
                    latitude = new_data['latitude']
                    longitude = new_data['longitude']
                    json_data = {"Id": id, "Ciudad": city, "Latitud": latitude, "Longitud": longitude}
                    path.append(json_data)
            length = nx.shortest_path_length(self.grafo, source, target, weight='weight')
            print(str(path))
            print(length)
            return {"Camino": path, "Total de Km": length}
        return False





# todas las rutas  for path in nx.all_simple_paths(G, source=0, target=3):
# Existe una ruta = nx.has_path(self.grafo, "Liberia", "Puerto Jimenez")
# todas las rutas cortas =  nx.all_shortest_paths(G,source=0,target=2)
#largo de la mas corta = nx.shortest_path_length(G,source=0,target=4
#nx.dijkstra_path(G,0,4)

'''
a = create_graph()
a.carga_de_nodos()
a.carga_de_aristas()
a.show_cities()
a.show_routes()

class accede_al_grafo:
    a = creacion_de_grafo()
    a.carga_de_nodos()
    a.carga_de_aristas()

    def ruta_mas_corta(self, id1, id2):
        b =nx.dijkstra_path(self.a.grafo, id1, id2)
        print(b)

'''



