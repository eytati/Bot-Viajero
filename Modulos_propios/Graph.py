import networkx as nx
import json

class create_graph:
    grafo = nx.Graph()
    instance = None

    def __init__(self):
        if not self.grafo.instance:
            self.grafo.instance = self

    def create_node(self, name, data_json):
        self.grafo.add_node(name, data_json)


    def create_edge(self, origin, destination, data_json):
        self.grafo.add_edge(origin, destination, data_json)

    def show_cities(self):
        cities = []
        for couter in self.grafo.node:
            graph_data = self.grafo.node[couter]
            if not graph_data == {}:
                city = graph_data['ciudad']
                cities.append(city)
        print(cities)
        return cities




'''
class accede_al_grafo:
    a = creacion_de_grafo()
    a.carga_de_nodos()
    a.carga_de_aristas()

    def ruta_mas_corta(self, id1, id2):
        b =nx.dijkstra_path(self.a.grafo, id1, id2)
        path_graph
        print(b)




a.ruta_mas_corta(18,16)
a.ruta_mas_corta(24,8)
a.ruta_mas_corta(2,5)
'''

'''


     def carga_de_aristas(self):
        aristas = []
        with open('edges2.json') as datos_json:
            aristas = json.load(datos_json)
        for contador in range(len(aristas["routes"])):
            peso = aristas['routes'][contador].get('weight')
            self.grafo.add_edge(aristas['routes'][contador].get('a'), aristas['routes'][contador].get('b'), weight= peso)


        def carga_de_nodos(self):
        nodos = []
        #collections_ciudades = string_connection.db.Ciudades
        with open('data2.json') as datos_json:
            nodos = json.load(datos_json)
            for contador in range(len(nodos["locations"])):
                city = nodos["locations"][contador].get('id')
                json_data = nodos["locations"][contador]
                self.grafo.add_node(city, json_data)
               # collections_ciudades.insert(json_data)

a = create_graph()
a.carga_de_nodos()
a.show_cities()
'''


